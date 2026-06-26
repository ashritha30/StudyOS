# from groq import Groq

# client = Groq(
#     api_key="abbbb"
# )

# def generate_study_content(pdf_text, instruction):

#     prompt = f"""
# {instruction}

# Study Notes:

# {pdf_text[:6000]}
# """

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )

#     return response.choices[0].message.content


import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_study_content(pdf_text, instruction):

    prompt = f"""
{instruction}

Study Notes:

{pdf_text[:6000]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content