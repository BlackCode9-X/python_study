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
def cost_optimized():
    # 将提示直接放入input函数
    dinner_pay_str = input("请输入晚餐总金额: ")
    tips_str = input("请输入小费比例(%): ")

    # 转换为数字
    dinner_pay = float(dinner_pay_str)
    tips_percentage = float(tips_str)

    # 计算
    tips_pay = dinner_pay * tips_percentage / 100
    total = dinner_pay + tips_pay

    print("-----账单详情------")
    # 使用 :.2f 格式化输出，保留两位小数
    print(f"账单金额：${dinner_pay:.2f}")
    print(f"小费比例：{tips_percentage}%")
    print(f"小费金额：${tips_pay:.2f}")
    print(f"总计金额：${total:.2f}")

if __name__ == '__main__':
    cost_optimized()
