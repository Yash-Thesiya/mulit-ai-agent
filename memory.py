class Memoryagent:
    def __init__(self):
        self.history = []
    
    def add(self, role: str, content: str):
        """New message history me add karo"""
        self.history.append({
            "role":role, 
            "content":content
            })
    def get_history(self) -> list:
        """Poori history return karo"""
        return self.history
    
    def get_context_string(self) -> str:
        """history ko readble string me convert karo (Research Agent ke liye)"""
        if not self.history:
            return "No previous conversation."
        lines = []
        for msg in self.history:
            prefix = "User" if msg["role"] == "user" else "Assistant"
            lines.append(f"{prefix}: {msg['content']}")
        return "\n".join(lines)
    
    def clear(self):
        """Session khatam - memory reset"""
        self.history = []
    
    def summary(self) -> str:
        return f"[Memory] {len(self.history)} message stored in this session."