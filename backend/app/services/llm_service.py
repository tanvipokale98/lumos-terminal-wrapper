from app.llm.huggingface_client import huggingface_client
from app.services.prompt import PromptService
class LLMService:

   def analyze_error(self,payload: dict) -> dict:
       prompt=PromptService().build_prompt(payload)
       response=huggingface_client.get_llm_response(prompt)
       return response

