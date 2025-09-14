"""
创建一个脚本，首先询问用户晚餐的总金额。

再询问用户希望支付的小费百分比（例如，输入15代表15%）。

计算出小费金额和含小费的总金额。

最后，以清晰、友好的格式打印出账单明细，例如：
    账单金额: $50.00
    小费比例: 15%
    小费金额: $7.50
    总计金额: $57.50

思考提示: 用户输入的都是字符串，你需要用 float() 或 int() 将它们转换成数字才能进行计算。
"""

"""
思路：
1. 发起问询，您今晚的晚餐总金额为多少？
2. 询问用户，支付的小费占总金额的百分比
3. 计算小费金额和总支出金额
"""
def cost():

    print("您今晚的晚餐总额是多少?")
    dinner_pay = input()

    print("小费占比?")
    tips = input()
    tips_pay = float(dinner_pay) * float(tips) / 100
    total = float(dinner_pay) + tips_pay
    print("-----bill------")
    print(f"账单金额：${dinner_pay}")
    print(f"小费比例：{tips}%")
    print(f"小费金额：${tips_pay}")
    print(f"总计金额：${total}")


if __name__ == '__main__':
    cost()
