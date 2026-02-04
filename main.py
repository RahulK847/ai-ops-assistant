from dotenv import load_dotenv
load_dotenv()

from agents.planner import create_plan
from agents.executor import execute_task    
from agents.verifier import verify_and_format

def main():
    user_request = input("Enter your request: ")

    plan = create_plan(user_request)
    print("Generated Plan:", plan)

    raw_results = execute_task(plan)
    print("Raw Results:", raw_results)
    
    final_output = verify_and_format(raw_results)
    print("Final Response:", final_output)

if __name__ == "__main__":
    main()