import json
import uuid
from pathlib import Path

SESSION_DIR = Path("lab1_2/sessions")

SESSION_DIR.mkdir(exist_ok=True)


class SessionManager:

    def create_session(self):

        session_id = str(uuid.uuid4())

        session = {
            "session_id": session_id,
            "messages": [],
            "summary": ""
        }

        self.save_session(session)

        return session

    def save_session(self, session):

        file = SESSION_DIR / f"{session['session_id']}.json"

        with open(file, "w", encoding="utf-8") as f:

            json.dump(
                session,
                f,
                indent=4
            )

    def load_session(self, session_id):

        file = SESSION_DIR / f"{session_id}.json"

        with open(file, encoding="utf-8") as f:

            return json.load(f)

    def append_message(
        self,
        session,
        role,
        content
    ):

        session["messages"].append(
            {
                "role": role,
                "content": content
            }
        )

    def summarize_session(
        self,
        session
    ):

        session["summary"] = (

            f"{len(session['messages'])} messages "
            "stored."

        )

    def fork_session(
        self,
        session
    ):

        new_session = {

            "session_id": str(uuid.uuid4()),

            "messages": list(
                session["messages"]
            ),

            "summary": session["summary"]

        }

        self.save_session(
            new_session
        )

        return new_session