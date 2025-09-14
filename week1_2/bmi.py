"""
任务要求:

编写一个脚本，接收用户的身高（单位：米）和体重（单位：公斤）。

根据BMI计算公式：BMI= kg/m*m，计算出用户的BMI指数。

将计算结果打印出来，保留两位小数。

请输入您的身高(m): 1.75
请输入您的体重(kg): 70
您的BMI指数为: 22.86
思考提示: 身高 ** 2 可以计算身高的平方。如何格式化输出，让浮点数只显示两位小数？

"""

def bmi():
    print("请输入您的身高(m): ")
    height = float(input())
    print("请输入您的体重(kg): ")
    weight = float(input())
    print(f"您的 BMI 指数为 {round(weight / height ** 2, 2)}")

if __name__ == '__main__':
    bmi()