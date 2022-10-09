from random import choice


class StackManager:

    def __init__(self):
        self.stack = list()
        self.pairs = list()

    def add_to_stack(self, chat_id: int) -> int:
        if self.stack:
            return self.find_pair(chat_id)
        else:
            self.stack.append(chat_id)
            return 0

    def remove_from_stack(self, chat_id: int) -> bool:
        if chat_id in self.stack:
            self.stack.remove(chat_id)
            return True
        else:
            return False

    def get_pair(self, chat_id: int) -> tuple:
        for pair in self.pairs:
            if chat_id in pair:
                return pair
        return ()

    def remove_pair(self, chat_id: int) -> tuple:
        pair = self.get_pair(chat_id)
        if pair:
            self.pairs.remove(pair)
        return pair

    def find_pair(self, first_chat_id: int) -> int:
        second_chat_id = choice(self.stack)
        if second_chat_id != first_chat_id:
            self.remove_from_stack(second_chat_id)
            pair = (first_chat_id, second_chat_id)
            self.pairs.append(pair)
            return second_chat_id
        return 0

    def get_second_user_from_pair(self, chat_id: int) -> int:
        pair = self.get_pair(chat_id)
        if pair:
            return pair[0] if pair[0] != chat_id else pair[1]
        return 0

