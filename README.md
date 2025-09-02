# AdminPriority Telegram Bot

## Quick start

1. Create virtual environment (optional but recommended)
   - Windows PowerShell:
     - `python -m venv .venv`
     - `.venv\\Scripts\\Activate.ps1`
2. Install dependencies
   - `pip install -r requirements.txt`
3. Configure environment
   - Copy `env.example` to `.env`
   - Put your token: `TELEGRAM_BOT_TOKEN=123456:ABC-...`
4. Run
   - `python bot.py`

## Notes
- The bot instantly shows greeting and menu when a user sends any text (no need to press /start). In groups, new members get the greeting automatically.
- Buttons open two sections: "Для админов, HR и закупщиков" and "Для партнёров" with the specified submenus and messages.

