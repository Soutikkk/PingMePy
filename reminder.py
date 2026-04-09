import time
import threading
import sys

# Try to use winsound for Windows, fallback to standard system bell for Mac/Linux
try:
    import winsound
    def play_sound():
        # Plays a beep at 1000 Hz for 500 milliseconds
        winsound.Beep(1000, 500)
except ImportError:
    def play_sound():
        # Standard system bell (may not work on all terminal emulators)
        print('\a', end='', flush=True)

def reminder_task(message, delay_in_seconds, show_countdown=False):
    """
    The function that handles the waiting and alerting.
    Can run with a countdown (blocking) or quietly in the background (non-blocking).
    """
    if show_countdown:
        # Loop backwards from delay_in_seconds down to 1
        for remaining in range(delay_in_seconds, 0, -1):
            # Print the countdown on the same line using \r (carriage return)
            sys.stdout.write(f"\r⏳ Countdown: {remaining} seconds remaining...   ")
            sys.stdout.flush()
            time.sleep(1)
        
        # Clear the countdown line once finished
        sys.stdout.write("\r" + " " * 50 + "\r") 
        sys.stdout.flush()
    else:
        # Just sleep quietly in the background
        time.sleep(delay_in_seconds)
        
    # Trigger the reminder!
    print(f"\n\n{'='*40}")
    print(f"⏰ REMINDER: {message}")
    print(f"{'='*40}\n")
    
    # Play a sound a few times to get attention
    for _ in range(3):
        play_sound()
        time.sleep(0.3)

def main():
    print("🌟 Welcome to the Simple Python Reminder App 🌟")
    print("-" * 45)
    
    # A list to keep track of our active background reminder threads (optional, but good practice)
    active_reminders = []

    while True:
        try:
            # 1. Get the message
            print("\n" + "-"*30)
            message = input("What should I remind you about? (or type 'quit' to exit): ")
            
            if message.lower() in ('quit', 'exit', 'q'):
                print("Goodbye!")
                break
                
            if not message.strip():
                print("Message cannot be empty. Try again.")
                continue
                
            # 2. Get the delay amount
            delay_input = input("Enter the delay time (e.g., 5): ")
            delay_value = float(delay_input)
            
            # 3. Get the time unit
            unit = input("Is that in (s)econds or (m)inutes? ").strip().lower()
            
            # Calculate total seconds
            if unit.startswith('m'):
                delay_in_seconds = int(delay_value * 60)
            else:
                # Default to seconds if they typed anything else
                delay_in_seconds = int(delay_value)
                
            # 4. Ask about the countdown
            # A countdown blocks the console, meaning they can't add another reminder until it finishes.
            countdown_choice = input("Show a countdown timer? Note: This will pause new inputs. (y/n): ").strip().lower()
            show_countdown = countdown_choice.startswith('y')
            
            # 5. Start the reminder
            if show_countdown:
                print(f"\n➡ Setting reminder for '{message}' in {delay_in_seconds} seconds...")
                # Run synchronously (blocks the loop until finished)
                reminder_task(message, delay_in_seconds, show_countdown=True)
            else:
                print(f"\n➡ Setting background reminder for '{message}' in {delay_in_seconds} seconds...")
                # Run asynchronously using a separate Thread (allows user to keep adding reminders)
                thread = threading.Thread(target=reminder_task, args=(message, delay_in_seconds, False))
                # daemon=True ensures the program can still exit even if background reminders are pending
                thread.daemon = True 
                thread.start()
                active_reminders.append(thread)
                
        except ValueError:
            print("❌ Invalid input: Please enter a valid number for the time.")
        except KeyboardInterrupt:
            # Catch Ctrl+C gracefully
            print("\nProgram interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()
