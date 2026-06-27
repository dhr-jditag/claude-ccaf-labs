from lab1_2.session_manager import SessionManager

manager = SessionManager()

print("=" * 60)
print("CREATE")
print("=" * 60)

session = manager.create_session()

print(session["session_id"])

print("=" * 60)
print("APPEND")
print("=" * 60)

manager.append_message(
    session,
    "user",
    "Investigate ransomware attack."
)

manager.append_message(
    session,
    "assistant",
    "Starting investigation."
)

manager.summarize_session(session)

manager.save_session(session)

print(session)

print("=" * 60)
print("LOAD")
print("=" * 60)

loaded = manager.load_session(
    session["session_id"]
)

print(loaded)

print("=" * 60)
print("FORK")
print("=" * 60)

fork = manager.fork_session(
    loaded
)

print(fork)