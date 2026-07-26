import json

import fastapi
from app.services.llm_service import LLMService
router=fastapi.APIRouter()

@router.post("/analyse")
def analyse(payload:dict)->dict:
    response=LLMService().analyze_error(payload)
    content = response.content
    content = content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)
            