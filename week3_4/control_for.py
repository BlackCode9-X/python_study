"""
任务要求:

编写一个脚本，接收用户输入的一段英文句子或单词。

遍历用户输入的字符串，统计其中元音字母（a, e, i, o, u，不区分大小写）的总数。

输出统计结果。例如，如果用户输入 Hello World，程序应输出：

您输入的句子中共有 3 个元音字母。
思考提示: 如何在循环中判断一个字符是否是元音字母？如何处理大小写问题？
"""

def count_vowels(text: str):
    # 使用字符串作为查找对象，更简洁
    # 在大量数据下，in 操作在集合中的查找速度会比列表更快
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count

if __name__ == '__main__':
    words = input("请输入一段英文句子或单词：")
    vowel_count = count_vowels(words)
    # 优化输出格式
    print(f"您输入的句子中共有 {vowel_count} 个元音字母。")