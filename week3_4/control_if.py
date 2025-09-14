"""
成绩等级评定器
这个练习旨在让你熟练使用 if-elif-else 结构来处理多种分支条件。

任务要求:

编写一个脚本，接收用户输入的百分制成绩（0-100的整数）。

根据以下规则，评定并输出对应的等级：

>= 90: 等级A

80-89: 等级B

70-79: 等级C

60-69: 等级D

< 60: 等级F

如果用户输入的不是0-100之间的数字，程序应输出错误提示。
"""
def grade_level(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    score = int(input("输入你的成绩："))
    print(grade_level(score))


