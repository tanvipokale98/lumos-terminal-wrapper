from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

class HuggingFaceClient:
    def get_llm_response(self, prompt: str) -> str:

        response = client.chat.completions.create(
    model="zai-org/GLM-5.2:novita",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
)
        return response.choices[0].message

huggingface_client=HuggingFaceClient()