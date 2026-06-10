<img width="1536" height="1024" alt="ChatGPT Image Jun 10, 2026, 03_03_23 PM" src="https://github.com/user-attachments/assets/63154bc0-8db9-4ea4-933c-88ebadcb2098" />

# Multi-Agent AI System

A Python-based Multi-Agent AI System that uses specialized agents to solve complex user queries by breaking them into smaller tasks, executing them through dedicated worker agents, storing intermediate results in memory, and generating a final synthesized response.

## Architecture

### Workflow

1. User submits a query.
2. Planner Agent breaks the query into subtasks.
3. Router Agent assigns tasks to appropriate worker agents.
4. Worker Agents perform research, web search, file reading, or calculations.
5. Results are stored in Memory Layer.
6. Synthesizer Agent combines all results.
7. Final answer is returned to the user.

---

## Project Structure

```text
project/
│
├── agents/
│   ├── planner.py
│   ├── router.py
│   ├── research.py
│   ├── tool.py
│   └── synthesizer.py
│
├── memory.py
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## Agents

### Planner Agent

Responsible for analyzing the user request and creating a list of subtasks.

Example:

User Query:

```text
Research the impact of AI in healthcare and give me:
- Key trends
- 3 real-world examples
- Risks
- Final summary
```

Planner Output:

```text
1. Find key trends
2. Find real-world examples
3. Identify risks
4. Create final summary
```

---

### Router Agent

Routes tasks to the correct worker agent or tool.

Responsibilities:

* Task assignment
* Workflow coordination
* Sequential execution
* Parallel execution (future enhancement)

---

### Research Agent

Performs LLM-based research and information gathering.

Used for:

* Trend analysis
* Summaries
* Explanations
* Research tasks

---

### Tool Agent

Provides access to external tools.

Supported Tools:

* Web Search
* File Reader
* Calculator

---

### Synthesizer Agent

Combines all intermediate results and generates a coherent final answer.

Responsibilities:

* Merge outputs
* Remove redundancy
* Generate structured reports

---

## Memory Layer

Stores intermediate outputs from all agents.

Example:

```text
Task 1 Result
Task 2 Result
Task 3 Result
Task 4 Result
```

The Synthesizer Agent uses these results to generate the final response.

---

## Features

* Multi-Agent Architecture
* Planner Agent
* Router Agent
* Research Agent
* Tool Agent
* Synthesizer Agent
* Memory Layer
* Modular Design
* Extensible Architecture
* OpenRouter Integration
* File Reading Support
* Calculator Tool
* Web Search Support

---

### Install Dependencies

```bash
pip install -r requirements.txt
pip install openai
pip install load_dotenv
```

### Create Environment File

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## Run

```bash
python main.py
```

---

## Example

Input:

```text
Analyze the smartphone market in 2026.
Provide:
1. Top brands
2. Market share
3. Emerging trends
4. AI features
5. Future predictions
6. Final summary
```

Output:
<img width="1468" height="614" alt="image" src="https://github.com/user-attachments/assets/e03c2b68-af68-4043-bc4b-1897aa99c167" />

##

---

## Technologies Used

* Python
* OpenRouter API
* OpenAI SDK
* JSON
* dotenv

---

## Author

Built as a learning project to understand Multi-Agent AI Systems, Agent Routing, Tool Calling, Memory Management, and Workflow Orchestration.
