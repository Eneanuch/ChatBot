import telebot
from config import *

bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(LOGGING_LEVEL)
