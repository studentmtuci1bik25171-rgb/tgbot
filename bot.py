import asyncio
import logging
import aiohttp
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os

# Импортируем ключи из .env
load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_model = os.getenv("OPENROUTER_MODEL")

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота
bot = Bot(token=telegram_token)
dp = Dispatcher()

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
openrouter_url = OPENROUTER_URL

async def get_cloud_ai_response(prompt: str) -> str:
    """Запрос к OpenRouter (облачный ИИ)"""
    try:
        timeout = aiohttp.ClientTimeout(total=10, connect=5, sock_read=5)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            headers = {
                "Authorization": f"Bearer {openrouter_api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": openrouter_model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 500
            }
            async with session.post(openrouter_url, json=payload, headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data['choices'][0]['message']['content'].strip()
                return None
    except Exception as e:
        logger.error(f"OpenRouter error: {e}")
        return None

# ===== ОСНОВНАЯ ФУНКЦИЯ ПОЛУЧЕНИЯ ОТВЕТА =====
async def get_ai_response(prompt: str) -> str:
    
    response = await get_cloud_ai_response(prompt)
    if response:
        return response
    
    return "❌ Извините, AI временно недоступен. Попробуйте позже."

# ===== КОМАНДЫ БОТА =====
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Привет! Я бот с ИИ.\n\n"
        "✅ Использую модель (google/gemma-4-31b-it:free)\n"
        "Просто напиши мне любое сообщение!"
    )

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Отправь любое сообщение — я отвечу.\n/start — приветствие")

@dp.message()
async def handle(message: types.Message):
    await bot.send_chat_action(message.chat.id, action="typing")
    response = await get_ai_response(message.text)
    await message.answer(response)

# ===== ЗАПУСК =====
async def main():
    logger.info("🚀 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())