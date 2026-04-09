# PingMePy ⏰

A simple, beginner-friendly Python reminder script running on the console. Set quick reminders, track them with an interactive countdown timer, or schedule multiple reminders to run quietly in the background!

## Features ✨

- **Simple & Intuitive**: A straightforward terminal interface that guides you step-by-step.
- **Multiple Timers**: Set multiple background reminders simultaneously without blocking the tool.
- **Live Countdown**: Option to display a real-time countdown timer directly on the console.
- **Cross-Platform Audio**: Plays an audible beep on completion (utilizing `winsound` for Windows and gracefully falling back to standard system bell on Linux/Mac).
- **Flexible Units**: Supports setting delays in both seconds and minutes.

## Requirements 📦

This script has **no external dependencies**. It's built entirely using Python's standard library:
- `time`
- `threading`
- `sys`

## How to Run 🚀

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Soutikkk/PingMePy.git
```
2. Navigate to the project directory:
```bash
cd PingMePy
```
3. Run the script using Python:
```bash
python reminder.py
```

## How to Use 📖

Once you run the script, simply answer the prompts:
1. Provide the message for what you wish to be reminded about.
2. Provide the delay value (e.g., `5`).
3. Set the unit type (Seconds or Minutes).
4. Decide if you wish to see a live visual countdown. 
   - *Note: Selecting "yes" will block you from taking further action until the timer wraps up.*
   - *Selecting "no" pushes the timer to the background so you can create even more reminders simultaneously!*

## Contributing 🤝

Contributions and feedback are welcome! Feel free to open issues or submit pull requests.

## License 📜

This project is open-source and free to use.
