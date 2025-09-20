"""
程序内部预先定义两个列表，分别代表两个不同部门的员工电子邮件地址。其中，有一些地址在两个列表中都出现了。

Python

# 示例数据
dev_department = ["a@test.com", "b@test.com", "c@test.com"]
qa_department = ["d@test.com", "a@test.com", "e@test.com"]
你的任务是：

找出所有不重复的员工邮件地址，并打印出来。

找出同时属于两个部门的员工邮件地址（即重复的地址），并打印出来。

思考提示: 如何利用集合的特性（自动去重、交集运算 &、并集运算 |）来轻松解决这个问题？
"""



def search_same_email(department1: list, department2: list):
    department1 = set(department1)
    department2 = set(department2)

    same_email = department1 & department2
    all_email = department1 | department2
    return same_email, all_email


def analyze_email_sets(list1: list, list2: list):
    set1 = set(list1)
    set2 = set(list2)

    # 交集
    common_emails = set1 & set2
    # 并集
    all_unique_emails = set1 | set2
    # 差集 (只在 list1 中)
    list1_only_emails = set1 - set2

    return all_unique_emails, common_emails, list1_only_emails


if __name__ == '__main__':
    dev_department = ["a@test.com", "b@test.com", "c@test.com", "shared@test.com"]
    qa_department = ["d@test.com", "a@test.com", "e@test.com", "shared@test.com"]

    all_emails, common, dev_only = analyze_email_sets(dev_department, qa_department)

    print("--- 邮件地址分析报告 ---")
    print(f"所有不重复的员工邮件: {all_emails}")
    print(f"同时属于两个部门的员工: {common}")
    print(f"仅属于开发部门的员工: {dev_only}")
    print("------------------------")

# if __name__ == '__main__':
#     dev_department = ["a@test.com", "b@test.com", "c@test.com"]
#     qa_department = ["d@test.com", "a@test.com", "e@test.com"]
#     same_email, all_email = search_same_email(dev_department, qa_department)
#     print(f"相同员工邮件：{same_email} \n 所有员工邮件{all_email}")

