import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

class Config:
    """Класс конфигурации бота"""
    
    # Токен Telegram бота (получить у @BotFather)
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    # API ключ OpenRouter
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
    
    # Настройки OpenRouter
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL = os.getenv('OPENROUTER_MODEL')
    
    # Настройки бота
    MAX_HISTORY_LENGTH = 10  # Максимальная длина истории диалога
    
    @classmethod
    def validate(cls):
        """Проверка наличия необходимых переменных"""
        if not cls.TELEGRAM_TOKEN:
            raise ValueError("TELEGRAM_TOKEN не установлен")
        if not cls.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY не установлен")