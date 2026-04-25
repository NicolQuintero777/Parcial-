from openai import OpenAI

client = OpenAI(
    api_key="sk-2d5996dc3b04479e9dacbf5d0085ce60",
    base_url="https://api.deepseek.com/v1"
)

contexto = """
Eres un chatbot experto en semiconductores y sistemas digitales en 2026.
Responde de forma clara, académica y bien explicada.
"""

def chatbot():
    print("🤖 Chatbot IA con DeepSeek\n")

    mensajes = [
        {"role": "system", "content": contexto}
    ]

    while True:
        user = input("Tú: ")

        if user.lower() == "salir":
            break

        mensajes.append({"role": "user", "content": user})

        try:
            respuesta = client.chat.completions.create(
                model="deepseek-chat",
                messages=mensajes
            )

            reply = respuesta.choices[0].message.content
            print("Bot:", reply, "\n")

            mensajes.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("⚠️ Error:", e)


chatbot()