from workflow import run_agent

def main():
    print("Debales AI Assistant (Advanced CLI)")
    while True:
        query = input("\nAsk something (or type 'exit'): ")
        if query.lower() == "exit":
            break

        answer = run_agent(query)
        print("\nAnswer:", answer)

if __name__ == "__main__":
    main()
