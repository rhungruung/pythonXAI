import openai  # pip install -U dotenv
from dotenv import load_dotenv
import os

load_dotenv()

# 設定 API 的 key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化對話歷史
messages = [{"role": "system", "content": "請用繁體中文進行後續對話"}]

while True:
    user_input = input("你：")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )

    assistant_message = response.choices[0].message.content
    print(f"AI：,{assistant_message}")

    messages.append({"role": "assistant", "content": assistant_message})
