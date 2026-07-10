import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()

# ✅ SQLite DB (auto created)
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)

# Initial state
initial_state = {
    "user_name": "User",
    "reminders": [],
}

async def main_async():
    APP_NAME = "Memory Agent"
    USER_ID = "default_user"

    # Check existing session
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    if existing_sessions and existing_sessions.sessions:
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"✅ Continuing session: {SESSION_ID}")
    else:
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"🆕 New session created: {SESSION_ID}")

    runner = Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    print("\n💬 Memory Agent Started (SQLite enabled)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("💾 Data saved in SQLite DB.")
            break

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

if __name__ == "__main__":
    asyncio.run(main_async())