import openai

openai.api_key_path = 'apikey.txt'
with open('text/www.centific.com.txt', "r", encoding="UTF-8") as f:
    context = f.read()

question = input("you: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"You are a helpful assistant. Answer the question based on the context below: \"{context}\""},
        {"role": "user", "content": f"{question}"},
    ]
)
print(response)
