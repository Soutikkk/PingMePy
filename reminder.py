import time
import threading
import sys

# Constants
BEEP_FREQUENCY = 1000
BEEP_DURATION = 500
BEEP_COUNT = 3
BEEP_GAP = 0.3


# Try Windows sound first
try:
    import winsound

    def play_sound():
        """Play a beep on Windows."""
        winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)

except ImportError:

    def play_sound():
        """Use the standard terminal bell on non-Windows systems."""
        print("\a", end="", flush=True)


def show_alert(message):
    """Display the reminder message and play an alert sound."""
    print("\n" + "=" * 40)
    print(f"⏰ REMINDER: {message}")
    print("=" * 40)

    for _ in range(BEEP_COUNT):
        play_sound()
        time.sleep(BEEP_GAP)


def countdown(seconds):
    """Display a countdown timer."""
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(
            f"\r⏳ Countdown: {remaining} seconds remaining...   "
        )
        sys.stdout.flush()
        time.sleep(1)

    # Clear the countdown line
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()


def reminder_task(message, delay, show_countdown=False):
    """Wait for the specified time and then trigger the reminder."""

    if show_countdown:
        countdown(delay)
    else:
        time.sleep(delay)

    show_alert(message)


def get_delay():
    """Get and validate the reminder delay from the user."""

    while True:
        try:
            value = float(input("Enter the delay time: "))

            if value <= 0:
                print("❌ Time must be greater than 0.")
                continue

            unit = input(
                "Is that in (s)econds or (m)inutes? "
            ).strip().lower()

            if unit.startswith("m"):
                return int(value * 60)

            if unit.startswith("s"):
                return int(value)

            print("❌ Please enter 's' for seconds or 'm' for minutes.")

        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    """Run the reminder application."""

    print("🌟 Welcome to the Simple Python Reminder App 🌟")
    print("-" * 45)

    active_reminders = []

    while True:
        try:
            print("\n" + "-" * 30)

            message = input(
                "What should I remind you about? "
                "(type 'quit' to exit): "
            ).strip()

            if message.lower() in {"quit", "exit", "q"}:
                print("Goodbye! 👋")
                break

            if not message:
                print("❌ Message cannot be empty.")
                continue

            delay = get_delay()

            countdown_choice = input(
                "Show a countdown timer? (y/n): "
            ).strip().lower()

            show_countdown = countdown_choice.startswith("y")

            if show_countdown:
                print(
                    f"\n➡ Setting reminder for '{message}' "
                    f"in {delay} seconds..."
                )

                # Countdown runs in the main thread
                reminder_task(
                    message,
                    delay,
                    show_countdown=True
                )

            else:
                print(
                    f"\n➡ Setting background reminder for "
                    f"'{message}' in {delay} seconds..."
                )

                # Background reminder
                thread = threading.Thread(
                    target=reminder_task,
                    args=(message, delay),
                    daemon=True
                )

                thread.start()
                active_reminders.append(thread)

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
