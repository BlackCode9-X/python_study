"""
任务要求:

程序在内部随机生成一个1到100之间的整数（你可能需要搜索一下如何使用 random 模块）。

使用 while 循环，不断提示用户输入猜测的数字。

根据用户的输入，给出“太大了”、“太小了”或“恭喜你，猜对了！”的提示。

当用户猜对时，游戏结束（即 while 循环终止）。

附加挑战： 记录用户总共猜了多少次，并在猜对后一并输出。


"""
import random

import random


def check_guess(guess, correct_number):
    """比较猜测数字和正确数字，并返回提示信息。"""
    if guess == correct_number:
        return "恭喜你，猜对了！"
    elif guess < correct_number:
        return "太小了"
    else:
        return "太大了"


if __name__ == '__main__':
    correct_answer = random.randint(1, 100)
    guess_count = 0

    # 使用 while True 和 break 的组合，是游戏循环的常用模式
    """
    避免使用“魔法字符串”: 
    while text != '恭喜你猜对了!' 
    这种写法依赖一个具体的字符串来控制循环，
    如果字符串不小心写错了，程序就会出问题。
    更稳健的方法是使用一个布尔值（True/False）作为标志。
    """
    while True:
        try:
            user_guess = int(input("输入你猜测的数字 (1-100)："))
            guess_count += 1

            result = check_guess(user_guess, correct_answer)
            print(result)

            # 如果猜对了，就跳出循环
            if user_guess == correct_answer:
                break
        except ValueError:
            print("请输入一个有效的数字！")

    print(f"你总共猜了 {guess_count} 次。")

