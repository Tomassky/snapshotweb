import logging
from math import e
from telegram import Update  
from telegram.ext import ContextTypes  
import os 

import config


log = logging.getLogger(__name__)

async def tg_search4mhtml(update: Update, context: ContextTypes.DEFAULT_TYPE):     
  try:  
    input_string = context.args[0].lower()
    """Note: 20240215 Didn't use the sqlite to search for the mhtml files, it could maybe cause a 'like' sql injection"""
    directory_path = os.path.join(config.ROOTPATH, "mhtmlfiles")
    filenames = os.listdir(directory_path) 
    matching_filenames = ''
    matching_filenames = [filename for filename in filenames if input_string in filename.lower()]

    if not matching_filenames:
      await context.bot.send_message(chat_id=update.effective_chat.id, text="No matching file")
    else:
      await context.bot.send_message(chat_id=update.effective_chat.id, text='\n'.join(matching_filenames))
  except Exception as Argument:
    logging.error(Argument)
    return ""