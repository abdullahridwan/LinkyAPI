from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")


def call_openAI(DESCRIPTION):
    client = OpenAI(api_key=config["KEY"])

    prompt = f"Given this description, come up with relevant tags that help identify it and output as a JSON with the key called tags: {DESCRIPTION}"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
    )
    return chat_completion.choices[0].message.content
