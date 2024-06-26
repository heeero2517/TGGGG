from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'your_bot_token'

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    context.user_data['first_name'] = user.first_name
    update.message.reply_text(
        f"Привет, {user.first_name}! Я бот. Как твоё полное имя? (Фамилия Имя Отчество)"
    )

def handle_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    context.user_data['full_name'] = text
    update.message.reply_text(f"Спасибо, {context.user_data['first_name']}. Твоё имя сохранено: {text}")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
