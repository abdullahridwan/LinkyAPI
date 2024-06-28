from openai import OpenAI
from dotenv import dotenv_values
import os
config = dotenv_values(".env")


def call_openAI(DESCRIPTION):
    client = OpenAI(api_key=os.environ.get('KEY'))

    prompt = """Given this description, come up with relevant tags that help identify it and output as a JSON. An example
JSON output looks like this {\"tags\": [\"Halal\", \"Brooklyn\"]}. Here is the description: """ + DESCRIPTION
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
