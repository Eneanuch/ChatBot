from telebot import types
from messages import *


start_keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard_button = types.KeyboardButton(START_DIALOG_PHRASE)
start_keyboard_markup.add(start_keyboard_button)

wait_keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
wait_keyboard_button_exit = types.KeyboardButton(EXIT_FROM_STACK_PHRASE)
wait_keyboard_markup.add(wait_keyboard_button_exit)

main_keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard_button_next = types.KeyboardButton(NEXT_USER_PHRASE)
main_keyboard_button_exit = types.KeyboardButton(EXIT_FROM_PAIR_PHRASE)
main_keyboard_markup.add(main_keyboard_button_next, main_keyboard_button_exit)
