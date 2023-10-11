import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update, context):
    await context.bot.send_message(chat_id=update.message.chat.id)