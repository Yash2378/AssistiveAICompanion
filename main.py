# main.py
from assistant import AICompanion

def main():
    # Initialize the AI Companion
    ai_companion = AICompanion()

    # Start listening for voice commands
    ai_companion.start_listening()

if __name__ == "__main__":
    main()
