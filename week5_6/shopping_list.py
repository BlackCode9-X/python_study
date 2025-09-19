"""
熟练掌握列表 (List) 的增、删、查、改等基本操作。
任务要求:
创建一个空的购物清单（一个列表）。
编写一个程序，循环提示用户进行操作：
输入 add <商品名> 可以向清单中添加商品。
输入 remove <商品名> 可以从清单中删除商品。
输入 show 可以打印出当前清单中的所有商品。
输入 quit 可以退出程序。
每次操作后都打印当前清单，以便用户查看。
"""

def shopping_list_manager():
    # 定义一个空的列表
    shopping_list = []
    while True:
        command = input("请输入指令: ")
        if command.startswith("add"):
            shopping_list.append(command.split("<")[1].rsplit(">")[0])
        elif command.startswith("remove"):
            shopping_list.remove(command.split("<")[1].rsplit(">")[0])
        elif command == "show":
            shopping_list.sort()
        elif command == "quit":
            break
        else:
            print("指令错误")
        print("----shopping list----")
        for i in shopping_list:
            print(i)

if __name__ == '__main__':
    shopping_list_manager()
