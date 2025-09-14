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
def get_grade_level(score):
    # 1. 首先进行输入验证
    if not 0 <= score <= 100:
        return "错误：请输入0到100之间的成绩。"

    # 2. 简化逻辑判断
    """
    类似 80 <= score < 90 的判断可以简化。因为程序是从上往下执行的，
    如果能进入这个 elif，说明 score >= 90 必然不成立，
    所以我们只需要判断 score >= 80 即可。
    """
    if score >= 90:
        return '等级A'
    elif score >= 80: # 无需检查 < 90
        return '等级B'
    elif score >= 70: # 无需检查 < 80
        return '等级C'
    elif score >= 60: # 无需检查 < 70
        return '等级D'
    else:
        return '等级F'

if __name__ == '__main__':
    try:
        score_input = int(input("输入你的成绩："))
        grade = get_grade_level(score_input)
        print(grade)
    except ValueError:
        # 处理用户输入非数字的情况
        print("错误：请输入一个有效的整数。")


