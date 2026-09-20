from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print("Bot:", response.text)