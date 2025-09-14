"""
任务要求:

程序在内部随机生成一个1到100之间的整数（你可能需要搜索一下如何使用 random 模块）。

使用 while 循环，不断提示用户输入猜测的数字。

根据用户的输入，给出“太大了”、“太小了”或“恭喜你，猜对了！”的提示。

当用户猜对时，游戏结束（即 while 循环终止）。

附加挑战： 记录用户总共猜了多少次，并在猜对后一并输出。


"""
import random


def guess_number(num: int):
    guess = int(input("输入你猜测的数字："))
    if guess == number:
        return "恭喜你猜对了!"
    if guess < number:
        return "太小了"
    if guess > number:
        return "太大了"


if __name__ == '__main__':
    number = random.randint(1, 101)
    text = ""
    count = 0
    while text != '恭喜你猜对了!':
        text = guess_number(number)
        print(text)
        count += 1
    print(count)


