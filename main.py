"""
Для запуска скрипта следует удостовериться, что все необходимые файлы для работы на месте
(папка с текстовыми документами, папки для текстов перевода, файл .env с ключами api)
Также требуется установить необходимые библиотеки для выполнения скрипта

Соединения с api может не работать в определенных случаях:
1) Не валидные ключи api
2) Региональные ограничения для исользования api
3) Проблемы с подключением к сети
"""

import os

from google import genai
from google.genai import types

from openai import OpenAI
from config import config

translated_text = "wait text"


def use_gemini():

    # Использование Gemini flash для перевода десяти текстов по машинному обучению из директории ml_texts
    client = genai.Client()
    os.environ["GOOGLE_API_KEY"] = config.GOOGLE_API_KEY

    # Чтение по очереди всех файлов в директории ml_texts
    for i in range(1, 11):
        path = os.path.join("ml_texts", f"ml_text_{i}.txt")
        with open(path, "r") as f:
            data = f.read()

        # Передача содержимого нейросети для перевода
        try:
            response = client.models.generate_content(
                model=config.GOOGLE_MODEL,
                config=types.GenerateContentConfig(system_instruction=config.TASK),
                contents=data,
            )
            translated_text = response.text
        except Exception as e:
            print(e)
            translated_text = (
                "Не удалось перевести текст из-за проблем с подключением к api"
            )

        # Запись перевода в файл
        transl_path = os.path.join("translated_gemini", f"ml_text_{i}.txt")
        with open(transl_path, "w", encoding="utf-8") as f:
            f.write(translated_text)


def use_deepseek():
    # Использование Deepseek для перевода десяти текстов по машинному обучению из директории ml_texts
    os.environ["DEEPSEEK_API_KEY"] = config.DEEPSEEK_API_KEY
    client = OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com"
    )

    # Чтение по очереди всех файлов в директории ml_texts
    for i in range(1, 11):
        path = os.path.join("ml_texts", f"ml_text_{i}.txt")
        with open(path, "r") as f:
            data = f.read()

        # Передача содержимого нейросети для перевода
        try:
            response = client.chat.completions.create(
                model=config.DEEPSEEK_MODEL,
                messages=[
                    {"role": "system", "content": config.TASK},
                    {"role": "user", "content": data},
                ],
                stream=False,
            )
            translated_text = response.choices[0].message.content
        except Exception as e:
            print(e)
            translated_text = (
                "Не удалось перевести текст из-за проблем с подключением к api"
            )

        # Запись перевода в файл
        transl_path = os.path.join("translated_deepseek", f"ml_text_{i}.txt")
        with open(transl_path, "w", encoding="utf-8") as f:
            f.write(translated_text)


def use_openai():
    # Использование OpenAI для перевода десяти текстов по машинному обучению из директории ml_texts
    os.environ["OPENAI_API_KEY"] = config.OPENAI_API_KEY
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"), base_url="https://api.openai.com"
    )

    # Чтение по очереди всех файлов в директории ml_texts
    for i in range(1, 11):
        path = os.path.join("ml_texts", f"ml_text_{i}.txt")
        with open(path, "r") as f:
            data = f.read()

        # Передача содержимого нейросети для перевода
        try:
            response = client.chat.completions.create(
                model="gpt-oss-120b",
                messages=[
                    {"role": "system", "content": "Translate next text into russian: "},
                    {"role": "user", "content": data},
                ],
                stream=False,
            )
            translated_text = response.choices[0].message.content
        except Exception as e:
            print(e)
            translated_text = (
                "Не удалось перевести текст из-за проблем с подключением к api"
            )

        # Запись перевода в файл
        transl_path = os.path.join("translated_openai", f"ml_text_{i}.txt")
        with open(transl_path, "w", encoding="utf-8") as f:
            f.write(translated_text)


def main():
    # Используем функции для перевода заранее заготовленных текстов
    use_gemini()
    use_deepseek()
    use_openai()


if __name__ == "__main__":
    main()
