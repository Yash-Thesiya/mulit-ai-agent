from agents.planner import Planneragent
from agents.router import Routeragent
from memory import Memoryagent
from agents.synthesizer import Synthesizeragent

def main():

    memory  = Memoryagent()
    planner = Planneragent()
    router  = Routeragent(memory = memory)
    synthesizer = Synthesizeragent()

    print("Multi-Agent System Ready! (type 'quit' to exit, 'memory' to see history)\n")

    while True:
        user_prompt = input("You : ").strip()

        if not user_prompt:
            continue

        if user_prompt.lower() == "quit":
            print("Byeee!")
            break

        if user_prompt.lower() == "memory":
            print("\n~~~~~~~ MEMORY ~~~~~~~")
            print(memory.get_context_string() or "Memory is empty.")
            print(memory.summary())
            continue
        # S-1 user mess memory me stored hua
        memory.add("user", user_prompt)
        # S - 2 planner 
        plan = planner.create_agent(user_prompt)
        print("\n===== PLAN =====")
        steps = plan.get("steps") or plan.get("Steps") or []

        for i, step in enumerate(steps, start=1):
            print(f"\nStep {i}")
            print(f"Type : {step.get('type')}")
            print(f"Task : {step.get('task')}")
        #S- 3 Router
        
        result = router.route(plan)

        print("\n===== RESULT =====")

        for i, item in enumerate(result, start=1):
            print(f"\nStep {i}")
            print(f"Task   : {item['task']}")
            print(f"Result : {item['result'][:200]}...")

        #S - 4 Synthesizer 
        print("\n===== SYNTHESIZING... =====")
        final_report = synthesizer.run(
            user_prompt=user_prompt,
            results=result,
            memory=memory
        )

        print("\n" + "=" * 76)
        print(final_report)
        print("=" * 76)

        #S - 5 Final report
        memory.add("assistant", final_report)
        print(f"\n{memory.summary()}")
        print("-" * 76)

if __name__ == "__main__":
    main()