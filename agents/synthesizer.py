from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

class Synthesizeragent:
    def run(self, user_prompt, results, memory=None):
        """
        user_prompt : original user ka sawaal
        results     : router se aaya list [{task, result}, ...]
        memory      :optional - pichha context
        """

        steps_text = ""
        for i, item in enumerate(results, start=1):
            steps_text += f"\nStep {i}: \n"
            steps_text += f" Task : {item['task']}\n"
            steps_text += f" Result : {item['result']}\n"

        memory_context = ""
        if memory and memory.get_history():
            memory_context = f"\n Previous Conversation:\n{memory.get_context_string()}\n"

            System_prompt = """
You are a Synthesizer Agent.
 
Your job:
- You receive a user's original question and results from multiple agents.
- Combine all results into one clean, structured report.
 
Output format (strict):
## 📋 Final Report
 
### 🎯 User Query
[restate the user's question briefly]
 
### 📊 Key Findings
[bullet points of important facts from all results]
 
### 🔍 Detailed Analysis
[paragraph or points expanding on findings]
 
### ✅ Conclusion
[final answer / recommendation in 2-3 lines]
 
Rules:
- Use the above headings exactly.
- Be concise but complete.
- Do NOT repeat raw data unnecessarily.
- Write in clear English.
"""
        user_message = f"""
Original User Question:
{user_prompt}
{memory_context}

Agent Results:
{steps_text}
 
Now synthesize all of this into a structured report.
"""
    
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role":"system", "content": System_prompt},
                {"role": "user", "content": user_message}    
            ]
        )
        return response.choices[0].message.content