# Telegram AI Bot

Telegram бот с интеграцией языковых моделей через OpenRouter API.

## Возможности

- 🤖 Асинхронная работа на aiogram
- 🧠 Поддержка различных LLM через OpenRouter
- 💬 Контекст диалога (история сообщений)
- 🐳 Полная контейнеризация в Docker
- 🔒 Безопасное хранение ключей через переменные окружения

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий
2. Установите зависимости: `pip install -r requirements.txt`
3. Создайте `.env` файл с вашими ключами
4. Запустите: `python bot.py`

### Запуск в Docker

```bash
# Сборка образа
docker build -t telegram-ai-bot .

# Запуск контейнера
docker run -d \
  --name telegram-bot \
  --restart unless-stopped \
  --env-file .env \
  telegram-ai-bot