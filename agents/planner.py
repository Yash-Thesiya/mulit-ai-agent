from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path =".env")
client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = os.getenv("OPENROUTER_API_KEY")
)

class Planneragent:
    def create_agent(self, user_prompt):
        system_prompt = """
            you are a planner Agent,

            your job:
            1. Understand the user's request.
            2. Create a step by step execution plan.
            3. Decide what type of task each step is.

            Possible types:
            - Research Agent (LLM based)
            - WEB Search 
            - File Reader
            - Calculator
            - Memory

            Return JSON only.

"""
        response = client.chat.completions.create(
            model = "openai/gpt-4o-mini",
            messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            response_format={"type": "json_object"}
        )

        raw = json.loads(response.choices[0].message.content)

        if "Steps" not in raw:
                for key in ["steps", "plan", "tasks", "STEPS"]:
                    if key in raw:
                        raw["Steps"] = raw[key]
                        break
        
        print("\n[DEBUG] Planner raw output:", json.dumps(raw, indent=2))
        return raw
