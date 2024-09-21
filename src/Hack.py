from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7710572619:AAHNd2MQg00xyZEab9BIq682IK_f1fbCaK8'
BOT_USERNAME: Final = '@ISK_mav_bot'


# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello this is bot for sending anonymous messages')


async def write_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Write the message to the channel')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is help command ')


# Responses

def handle_response(text:str) -> str:
    processed:str = text.lower()
    if '' in processed:
        return 'sent'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type #says the type of chat
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('write', start_command))
    app.add_handler(CommandHandler('help', start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # polls the bot
    print('Poling...')
    app.run_polling(poll_interval=3)