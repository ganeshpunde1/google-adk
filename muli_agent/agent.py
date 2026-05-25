"""Multi-agent application for handling greetings, farewells, and weather requests."""

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import Session
from google.adk.memory import InMemoryMemoryService
from dotenv import load_dotenv

load_dotenv()

# Model configuration
ROOT_AGENT_MODEL = "gemini-1.5-pro"
SUB_AGENT_MODEL  = "gemini-1.5-flash"

# Session configuration
APP_NAME = "first_application_to_test_agents"
USER_ID = "user_1"
SESSION_ID = "session_001"

session_service = InMemoryMemoryService()

session = Session(
    app_name=APP_NAME,
    user_id=USER_ID,
    id=SESSION_ID
)

session = session_service.add_session_to_memory(session=session)



def say_hello(name: str = "there") -> str:
    """Provides a simple greeting, optionally addressing the user by name.

    Args:
        name: The name of the person to greet. Defaults to "there".

    Returns:
        A friendly greeting message.
    """
    print(f"--- Tool: say_hello called with name: {name} ---")
    return f"Hello, {name}!"


def say_goodbye() -> str:
    """Provides a simple farewell message to conclude the conversation."""
    print(f"--- Tool: say_goodbye called ---")
    return "Goodbye! Have a great day."


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city: The name of the city for which to retrieve the weather report.

    Returns:
        A dict with status and result or error message.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees "
                "Celsius (41 degrees Fahrenheit)."
            ),
        }
    return {
        "status": "error",
        "error_message": f"Weather information for '{city}' is not available."
    }


# Greeting agent - handles user greetings
greeting_agent = Agent(
    model=SUB_AGENT_MODEL,
    name="greeting_agent",
    description="Handles simple greetings and hellos using the 'say_hello' tool.",
    instruction=(
        "You are the Greeting Agent. Your ONLY task is to provide a friendly greeting.\n"
        "Use the 'say_hello' tool to generate the greeting.\n"
        "If the user provides their name, make sure to pass it to the tool.\n"
        "Do not engage in any other conversation or tasks."
    ),
    tools=[say_hello],
)

# Farewell agent - handles user farewells
farewell_agent = Agent(
    model=SUB_AGENT_MODEL,
    name="farewell_agent",
    description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
    instruction=(
    "You are the Farewell Agent. Your ONLY task is to provide a polite farewell message.\n"
    "Use the 'say_goodbye' tool when the user indicates they are leaving\n"
    "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you').\n"
    "Do not perform any other actions."
),
tools=[say_goodbye],
)



# Root agent - main coordinator
root_agent = Agent(
    name="Root_Agent",
    model=ROOT_AGENT_MODEL,
    description="Main coordinator. Handles weather requests and delegates greetings/farewells.",
    instruction=(
        "You are the main Weather Agent coordinating a team. Your primary responsibility "
        "is to provide weather information.\n"
        "Use the 'get_weather' tool ONLY for specific weather requests (e.g., 'weather in London').\n"
        "You have specialized sub-agents:\n"
        "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'.\n"
        "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'.\n"
        "Analyze the user's query and delegate appropriately.\n"
        "For anything else, respond appropriately or state you cannot handle it."
    ),
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent],
)


# Initialize the runner
runner_root = Runner(
    app_name=APP_NAME,
    session_service=session_service,
    agent=root_agent,
)
