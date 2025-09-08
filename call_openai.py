import os
import openai

def call_openai():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY is missing!")
    print("OpenAI API key is present ✔")

    messages = [
        {"role": "system", "content": "You are a helpful GitHub Actions assistant."},
        {"role": "user", "content": "Say hello from GitHub Actions!"}
    ]

    print("System prompt:", messages[0]['content'])
    print("User prompt:", messages[1]['content'])

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            api_key=key
        )
        print("OpenAI response:", response.choices[0].message.content)
    except Exception as e:
        print("OpenAI call failed, but workflow continues:", e)

# Call the function
if __name__ == "__main__":
    call_openai()
