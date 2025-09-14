"""
这个练习将帮助你理解类型转换以及整除 (//) 和取余 (%) 运算符的妙用。

任务要求:

编写一个脚本，接收用户输入的总秒数（一个整数）。

计算这个秒数相当于多少小时、多少分钟、以及剩余多少秒。

输出结果，例如，如果用户输入3661，程序应输出：

3661秒 = 1小时, 1分钟, 1秒

思考提示: 1小时有3600秒，1分钟有60秒。如何使用 // 得到商，使用 % 得到余数？

hour = 3661 // 3600 = 1   3661 % 3600 = 61
minute = 3661 % 3600 // 60 = 1
second = 3661 % 3600 % 60 = 1

"""

def time_cover_optimized():
    total_sec = int(input("请输入总秒数: "))

    # 首先计算小时
    hours = total_sec // 3600
    # 计算除去小时后剩下的秒数
    remaining_seconds = total_sec % 3600

    # 在剩下的秒数里计算分钟
    minutes = remaining_seconds // 60
    # 最后计算剩下的秒数
    seconds = remaining_seconds % 60

    print(f"{total_sec}秒 = {hours}小时, {minutes}分钟, {seconds}秒")

if __name__ == '__main__':
    time_cover_optimized()

