from agents.research import Researchagent
from agents.tool import Toolagent

class Routeragent:
    def __init__(self, memory=None):

        self.research = Researchagent()
        self.tool = Toolagent()
        self.memory = memory

    
    def route(self, plan):
        steps = plan.get("Steps") or plan.get("steps") or []
        output = []

        for step in steps:
            tasks_type = step.get("type")
            task = step.get("task")

            if tasks_type =="Research Agent":
                result = self.research.run(task, memory=self.memory)
            
            elif tasks_type == "Memory":
                result = self.memory.get_context_string() if self.memory else "Memory not available."

            elif tasks_type in ["Web search", "File Reader","Calculator"]:
                if "search" in tasks_type.lower():
                    normalized = "Web search"
                elif "file" in tasks_type.lower():
                    normalized = "File Reader"
                elif "calc" in tasks_type.lower():
                    normalized = "Calculator"
                else:
                    normalized = tasks_type
                    result = self.tool.run(normalized, task)

            else:
                result = f"Unknown task type: {tasks_type}"

            if self.memory:
                self.memory.add("assistant", f"[{tasks_type}] {result}")

            output.append({"task": task,"result": result})
            
        return output