from telegram import Update  
from telegram.ext import ContextTypes  
import logging

log = logging.getLogger(__name__) 

async def tg_start(update: Update, context: ContextTypes.DEFAULT_TYPE):  
    await context.bot.send_message(chat_id=update.effective_chat.id,  
                                   text=f"这是一个tg机器人，测试连通性")  