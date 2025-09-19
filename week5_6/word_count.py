"""
任务要求:
编写一个脚本，接收用户输入的一段长英文文本。
将文本分割成单词（可以简单地用空格分割，标点符号可以暂时忽略）。
使用一个字典来统计每个单词出现的次数。字典的 key是单词，value是该单词出现的频率。
最后，打印出这个字典。例如，输入 hello world hello python，应输出类似 {'hello': 2, 'world': 1, 'python': 1} 的结果。
思考提示: 当遍历到一个单词时，如何判断这个单词是否已经在字典的 key 中了？如果在了，怎么更新它的value？如果不在，又该怎么操作？
"""
import re


def count_words(text: str):
    word_count = dict()
    if re.match(r"^[A-Za-z]+(?: [A-Za-z]+)*$", text):
        words = text.split(" ")
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    else:
        print("输入错误！")
    return word_count

if __name__ == '__main__':
    print(count_words("hello world hello python"))
    count_words("hello world hello 你好")
