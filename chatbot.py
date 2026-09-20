import os
import time
from dotenv import load_dotenv
from google import genai

# Load environment variables from chatbot.env or .env
load_dotenv("chatbot.env")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("YOUR_API_KEY")

if not api_key or api_key == "YOUR_API_KEY":
    print("Error: Please set your API key in chatbot.env or .env file.")
    exit(1)

model_name = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
client = genai.Client(api_key=api_key)
chat = client.chats.create(model=model_name)

print("Chatbot initialized! Type 'exit' to quit.\n")

while True:
    try:
        question = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")
        break

    if not question:
        continue

    if question.lower() == "exit":
        print("Goodbye!")
        break

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = chat.send_message(question)
            print(f"Bot: {response.text}\n")
            break
        except Exception as e:
            if "503" in str(e) and attempt < max_retries - 1:
                time.sleep(2)
                continue
            print(f"Bot Error: {e}\n")
            break



