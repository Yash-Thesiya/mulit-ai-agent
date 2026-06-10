from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

class Researchagent:
    def run(self, task, memory=None):
        if memory and memory.get_history():
            context = memory.get_context_string()
            full_task = f"Previous conversation: \n{context}\n\nNew task: {task}"
        else:
            full_task = task
            
        response = client.chat.completions.create(
            model = "openai/gpt-oss-20b:free",
            messages =[
                {
                    "role":"system",
                    "content":"You are a helpful research assistant."
                },
                {
                    "role":"user",
                    "content": task
                }
            ]
        )
        return response.choices[0].message.content