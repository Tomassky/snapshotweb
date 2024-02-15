import logging
from telegram import Update  
from telegram.ext import ContextTypes  
 
from lib import exist, save
import config

log = logging.getLogger(__name__)

async def tg_url2mhtml(update: Update, context: ContextTypes.DEFAULT_TYPE):     
  try:  
    url = context.args[0]
    if url and url.startswith('http') and url.count('://') == 1:
      log.info("prepare to save the url: " + url)
      if not exist.url_is_exist(url): 
        save.save_page(url)      
      await context.bot.send_message(chat_id=update.effective_chat.id, text=config.SUCCESSCONTENT)
    else:
      await context.bot.send_message(chat_id=update.effective_chat.id, text=config.HTTPFAILCONTENT)
  except Exception as Argument:
    log.error(Argument)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=config.HTTPFAILCONTENT)