import os
from dotenv import load_dotenv
from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner
from pydantic import BaseModel
import asyncio

# Load environment variables from .env file
load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="You are a homework detector. A question is considered 'homework' if it asks for factual information, educational content, or could be related to school assignments. This includes historical facts, math problems, science questions, etc. Be inclusive - if it could reasonably be homework, mark it as homework.",
    output_type=HomeworkOutput,
    model="gpt-4o-mini",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
    model="gpt-4o-mini",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
    model="gpt-4o-mini",
)


async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    
    # Debug output
    print(f"Guardrail check for: '{input_data}'")
    print(f"Is homework: {final_output.is_homework}")
    print(f"Reasoning: {final_output.reasoning}")
    print(f"Tripwire triggered: {not final_output.is_homework}")
    print("-" * 30)
    
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
    model="gpt-4o-mini",
)

async def main():
    # Test 1: Historical question (should pass guardrail)
    print("Processing: 'who was the first president of the united states?'")
    try:
        result = await Runner.run(triage_agent, "who was the first president of the united states?")
        print("Response:", result.final_output)
    except Exception as e:
        print(f"Request blocked: {e}")
    
    print("=" * 50)

    # Test 2: Philosophical question (should be blocked)
    print("Processing: 'what is life'")
    try:
        result = await Runner.run(triage_agent, "what is life")
        print("Response:", result.final_output)
    except Exception as e:
        print(f"Request blocked: {e}")

if __name__ == "__main__":
    asyncio.run(main())