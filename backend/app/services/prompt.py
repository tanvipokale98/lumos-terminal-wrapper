
class PromptService:
    def build_prompt(self, payload: dict) -> str:
        
        prompt = f"Ypu are expert code reviewer. Analyze the following {payload.get('language')} error:\n{payload}."
        prompt+="Please provide a detailed analysis of the error, including error explanation in detail so user can understand,root cause, potential solutions,confidencescore, and any relevant code snippets or references that could help in resolving the issue. Your response should be clear, concise, and structured in a way that is easy to understand for developers of varying skill levels. Return your response in a JSON format with the following keys: errorSummary, rootCause, debuggingSteps, confidence. Ensure that the debugging steps are actionable and practical for a developer to follow."
        return prompt