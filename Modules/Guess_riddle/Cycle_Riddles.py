
import Guess


RIDDLE_DICT = {"Этот рыжий господин - вскусный, сладкий...": ["апельсин", "мандарин"],
                   "Бегут полоски, загнув носки": ["лыжи"],
                   "Зимой и летом одним цветом": ["елка", "ель","сосна", "пихта", "туя"],
                   "Мягки лапки, а в лапках царапки": ["кошечка", "кошка", "кот"]}


def cycle_of_riddles(my_dict):
    for key, value in my_dict.items():
        if guess.guess_the_riddle(key, value):
            print("Угадали!")
        else:
            print("Увы :(")


cycle_of_riddles(RIDDLE_DICT)
