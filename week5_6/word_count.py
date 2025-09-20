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
    """
    正则表达式的限制: 你使用的 re.match(r"^[A-Za-z]+(?: [A-Za-z]+)*$, text)` 有两个问题：
        re.match 只从字符串的开头匹配，如果开头有空格，就会匹配失败。
        这个表达式不允许任何标点符号，使得它在处理真实文本时非常受限。例如 "hello world." 就会被拒绝。
    更简洁的计数方法: Python字典的 .get() 方法可以让计数逻辑变得更优雅。word_count.get(word, 0) 的意思是“尝试获取 word 的值，如果它不存在，就返回默认值0”。
    处理标点符号: 真实场景下，我们需要先将文本中的标点符号替换为空格或直接移除，然后再进行分割。
    """
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


def count_words_v2(text: str):
    # 1. 预处理文本：转为小写，并用正则表达式替换所有非字母数字的字符为空格
    # \W+ 匹配一个或多个非字母数字字符
    cleaned_text = re.sub(r'\W+', ' ', text.lower())

    # 2. 分割单词
    words = cleaned_text.split()

    word_count = {}

    # 3. 使用更Pythonic的 .get() 方法进行计数
    for word in words:
        if word:  # 确保不是空字符串
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

if __name__ == '__main__':
    # print(count_words("hello world hello python"))
    # count_words("hello world hello 你好")
    text1 = "Hello world, hello python! Python is great."
    text2 = "  leading space and trailing space  "
    print(f"'{text1}' 的词频统计: {count_words_v2(text1)}")
    print(f"'{text2}' 的词频统计: {count_words_v2(text2)}")