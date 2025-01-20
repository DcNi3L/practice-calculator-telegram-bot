from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from dotenv import load_dotenv
import os
from sympy import sympify, Symbol, pi, E

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

if not API_TOKEN:
    raise ValueError("Токен API не найден! Убедитесь, что он указан в .env файле.")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

user_history = {}

def calculate(expression):
    try:
        # sympify преобразует строку в математическое выражение
        result = sympify(expression).evalf()
        return result
    except Exception as e:
        return f"Ошибка: {e}"

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_history[user_id] = []  # Инициализируем историю пользователя
    await message.reply(
        "Привет! Я научный калькулятор-бот. Введи выражение, и я посчитаю его.\n"
        "Доступные команды:\n"
        "/help - Список доступных функций\n"
        "/history - Показать историю вычислений\n"
        "/clear_history - Очистить историю"
    )

# Команда /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(
        "Я поддерживаю научные вычисления, включая:\n"
        "- Арифметика: +, -, *, /, **, //, %\n"
        "- Логарифмы: log(x, base), ln(x)\n"
        "- Тригонометрия: sin, cos, tan, asin, acos, atan\n"
        "- Постоянные: pi, e\n"
        "- Корни: sqrt(x)\n\n"
        "Просто введи выражение, например:\n"
        "`2 * pi * 10`\n"
        "`sqrt(16)`\n"
        "`log(100, 10)`\n"
        "`sin(pi / 2)`\n\n"
        "Для просмотра истории используй /history.",
        parse_mode=ParseMode.MARKDOWN,
    )

# Команда /history
@dp.message_handler(commands=['history'])
async def send_history(message: types.Message):
    user_id = message.from_user.id
    history = user_history.get(user_id, [])
    if history:
        history_message = "\n".join(history[-10:])  # Показываем последние 10 операций
        await message.reply(f"Ваша история вычислений:\n{history_message}")
    else:
        await message.reply("История пуста.")

# Команда /clear_history
@dp.message_handler(commands=['clear_history'])
async def clear_history(message: types.Message):
    user_id = message.from_user.id
    user_history[user_id] = []
    await message.reply("История очищена.")

# Обработчик текстовых сообщений (вычисления)
@dp.message_handler()
async def calculate_expression(message: types.Message):
    user_id = message.from_user.id
    expression = message.text

    # Выполняем вычисление
    result = calculate(expression)
    if isinstance(result, (int, float, Symbol)):
        # Сохраняем результат в историю
        user_history.setdefault(user_id, []).append(f"{expression} = {result}")
        await message.reply(f"Результат: <b>{result}</b>", parse_mode=ParseMode.HTML)
    else:
        await message.reply(result)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
