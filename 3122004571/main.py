import jieba
import difflib
from collections import Counter
from math import sqrt


def cos_similarity(text1, text2):
    # 余弦相似度算法可以通过分析两段话的词语频率判断是否抄袭，但是文本长度较长的话，偏差会比较大

    # 借助jieba库将词语分组
    article1 = list(jieba.cut(text1))
    article2 = list(jieba.cut(text2))

    # 计算词语出现的频率
    freq1 = Counter(article1)
    freq2 = Counter(article2)

    # 计算余弦相似度
    dot_product = sum(freq1[word] * freq2[word] for word in freq1)
    norm1 = sqrt(sum(freq1[word] ** 2 for word in freq1))
    norm2 = sqrt(sum(freq2[word] ** 2 for word in freq2))
    return dot_product / (norm1 * norm2)

def diff_similarity(text1, text2):
    #difflib库提供了便捷的文本比较方法，但对于语句顺序替换抄袭识别较差
        matcher = difflib.SequenceMatcher(None, text1, text2)
        return matcher.ratio()

def test1():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_add.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity=(similarity1+similarity2)/2
    with open(result, 'w') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test2():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_del.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test3():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_1.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test4():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_10.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test5():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_15.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test6():
    text1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    text2 = "这是一句话，一句没意义的话，可以用作测试，验证可行性。 "
    result = 'D:/result.txt'
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test7():
    text1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    text2 = "这是一句话，一句有意义的话，用作测试验证此程序的可行性。 "
    result = 'D:/result.txt'
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))


def test8():
    text1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    text2 = "一二三四五六七，数来数去数不清。 "
    result = 'D:/result.txt'
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test9():
    text1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    text2 = "这是一句抄袭的话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    result = 'D:/result.txt'
    similarity1 = cos_similarity(text1, text2)
    similarity2 = diff_similarity(text1, text2)
    similarity = (similarity1 + similarity2) / 2
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))


def main():
   test1()
   test2()
   test3()
   test4()
   test5()
   test6()
   test7()
   test8()
   test9()

if __name__ == '__main__':
  main()






