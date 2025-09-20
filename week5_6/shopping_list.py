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
    """
        指令解析不够健壮: 你的代码 command.split("<")[1].rsplit(">")[0] 强依赖于用户输入 < 和 >。如果用户输入 add apple，程序就会因为找不到 < 而崩溃。我们需要一种更通用的方式来解析指令。
        remove 操作的风险: 如果用户尝试移除一个清单中不存在的商品，.remove() 方法会抛出 ValueError 并导致程序崩溃。我们需要先检查商品是否存在。
        show 的行为: show 指令的行为是 shopping_list.sort()，这会原地修改列表的顺序，但并没有打印任何东西。用户的意图应该是查看列表，而不是排序。
        用户体验: 每次操作后都打印清单，可以给用户更及时的反馈。
    """
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


def shopping_list_manager_v2():
    shopping_list = []
    print("--- 欢迎使用购物清单管理器 (v2) ---")
    print("指令示例: add apple, remove milk, show, quit")

    while True:
        command_input = input("请输入指令 > ").strip().lower()
        parts = command_input.split(' ', 1)
        action = parts[0]

        if action == 'quit':
            print("感谢使用，再见！")
            break

        elif action == 'show':
            print("\n--- 当前购物清单 ---")
            if not shopping_list:
                print("清单是空的！")
            else:
                # 使用 enumerate 来创建带编号的列表
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            print("--------------------\n")

        elif action == 'add':
            # 可以增加输入限定
            if len(parts) > 1 and parts[1]:
                item = parts[1].strip()
                shopping_list.append(item)
                print(f"已添加: '{item}'")
            else:
                print("错误: 'add' 指令需要提供商品名。")

        elif action == 'remove':
            if len(parts) > 1 and parts[1]:
                item = parts[1].strip()
                # 关键：先检查是否存在
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"已移除: '{item}'")
                else:
                    print(f"错误: 清单中找不到 '{item}'。")
            else:
                print("错误: 'remove' 指令需要提供商品名。")

        else:
            print(f"未知指令: '{action}'")


if __name__ == '__main__':
    # shopping_list_manager()
    shopping_list_manager_v2()