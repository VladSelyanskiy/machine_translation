import os
from dotenv import load_dotenv


class Config:

    # Загрузка переменных из файла .env
    load_dotenv()

    # Первая модель
    # Настройки для работы с
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_MODEL: str = "gemini-2.5-flash"

    # Вторая модель
    # Настройки для работы с Deepseek
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_MODEL: str = "deepseek-chat"

    # Третья модель
    # Настройки для работы
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = "gpt-oss-120b"

    # Задание
    TASK: str = "Translate next text into russian: "


config = Config()
