from pathlib import Path

class Toolagent:
    def run(self, tool_type, task):
          
        if tool_type == "Web Search":
            return self.web_search(task)
        elif tool_type == "File Reader":
            return self.file_reader(task)
        elif tool_type == "Calculator":
            return self.calculatro(task)
        return "Unknown tool"
     
    def web_search(self, query):
        return f"Mock web Sreach result for: {query}"
    
    def file_reader(self, filepath):
        try:
            path = Path(filepath)

            if not path.exists():
                return "File not Found"
            return path.read_text(
                encoding="utf-8"
            )
        except Exception as e:
            return str(e)
        
    def calculatro(self, expression):

        try:
            return eval(expression)
        except Exception as e:
            return str(e)

               