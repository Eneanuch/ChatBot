from bot import bot
from keyboard import *
from stack_manager import StackManager

stack_manager = StackManager()


@bot.message_handler(commands=["start"])
def handle_start_message(message):
    bot.send_message(message.chat.id,
                     START_MESSAGE,
                     reply_markup=start_keyboard_markup)


@bot.message_handler(func=lambda message: message.text == START_DIALOG_PHRASE, content_types=['text'])
def handle_start_dialog(message):
    bot.send_message(message.chat.id,
                     FIND_PAIR_MESSAGE)
    second_user_chat_id = stack_manager.add_to_stack(chat_id=message.chat.id)
    if second_user_chat_id:
        bot.send_message(message.chat.id,
                         FOUND_PAIR_MESSAGE, reply_markup=main_keyboard_markup)
        bot.send_message(second_user_chat_id,
                         FOUND_PAIR_MESSAGE, reply_markup=main_keyboard_markup)
    else:
        bot.send_message(message.chat.id, WAIT_MESSAGE, reply_markup=wait_keyboard_markup)


@bot.message_handler(func=lambda message: message.text == EXIT_FROM_STACK_PHRASE, content_types=['text'])
def handle_exit_from_stack(message):
    if stack_manager.remove_from_stack(message.chat.id):
        bot.send_message(message.chat.id,
                         SUCCESS_EXIT_FROM_STACK_MESSAGE,
                         reply_markup=start_keyboard_markup)
    else:
        handle_start_message(message)


@bot.message_handler(func=lambda message: message.text == EXIT_FROM_PAIR_PHRASE, content_types=['text'])
def handle_exit_from_pair(message):
    pair = stack_manager.remove_pair(message.chat.id)
    if pair:
        second_user_chat_id = pair[0] if pair[0] != message.chat.id else pair[1]
        bot.send_message(second_user_chat_id, USER2_EXIT_FROM_PAIR_MESSAGE, reply_markup=start_keyboard_markup)
        bot.send_message(message.chat.id, SUCCESS_EXIT_FROM_PAIR_MESSAGE, reply_markup=start_keyboard_markup)
    else:
        handle_start_message(message)


@bot.message_handler(func=lambda message: message.text == NEXT_USER_PHRASE, content_types=['text'])
def handle_next_user(message):
    pair = stack_manager.remove_pair(message.chat.id)
    if pair:
        second_user_chat_id = pair[0] if pair[0] != message.chat.id else pair[1]
        bot.send_message(second_user_chat_id, USER2_EXIT_FROM_PAIR_MESSAGE, reply_markup=start_keyboard_markup)
        handle_start_dialog(message)
    else:
        handle_start_message(message)


@bot.message_handler()
def handle_send_message(message):
    second_user = stack_manager.get_second_user_from_pair(message.chat.id)
    if second_user:
        bot.send_message(second_user, message.text)
    else:
        handle_start_message(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
