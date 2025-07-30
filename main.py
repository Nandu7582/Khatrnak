# main.py
import time
import threading
from src.telegram_bot import start_bot
from src.scheduler import run_scheduler

def main():
    print("📡 Pocket Option Signal Bot Starting...")

    # Start Telegram bot listener (if any commands needed)
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Start scheduler for signal predictions
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    print("✅ Bot is running. Waiting for signals...")

    # Keep the app alive (very important for Render)
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("🛑 Bot stopped manually.")

if __name__ == "__main__":
    main()
