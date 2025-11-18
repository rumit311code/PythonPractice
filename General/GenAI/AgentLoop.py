import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

def agent_loop(max_turns=5):
    turn_count = 1
    while turn_count <= max_turns:
        print(f"Turn {turn_count} - Agent listening...")
        user_input = input("You: ")
        response = generate_text(user_input)
        print(f"Agent: {response}")
        turn_count += 1

if __name__ == "__main__":
    agent_loop()
