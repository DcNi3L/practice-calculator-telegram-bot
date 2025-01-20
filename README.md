# Telegram Scientific Calculator Bot

A Telegram bot that performs basic and scientific calculations using Python and SymPy.

---

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division, etc.
- **Scientific Functions**:
  - Trigonometric functions (`sin`, `cos`, `tan`, etc.).
  - Logarithms (`log`, `ln`).
  - Constants (`pi`, `e`).
  - Roots and powers (`sqrt`, `**`).
- **History**: View and manage your calculation history.
- **Error Handling**: Safely processes user input with clear error messages.

---

## Commands

- **`/start`**: Start the bot and initialize your session.
- **`/help`**: View available features and usage instructions.
- **`/history`**: Display the last 10 calculations.
- **`/clear_history`**: Clear your calculation history.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/calculator-bot.git
   cd calculator-bot
   ```
2. Add your Telegram Bot Token to a `.env` file:

   ```env
   API_TOKEN=your_telegram_bot_token
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```
4. Open Telegram and interact with your bot!

---

This project is licensed under the MIT License. See LICENSE for details.
