import jieba
from collections import Counter
from math import sqrt

def calculate_similarity(file1, file2):
    # 读取文本文件
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()

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


def test1():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_add.txt'
    result = 'D:/result.txt'
    similarity = calculate_similarity(file1, file2)
    with open(result, 'w') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test2():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_del.txt'
    result = 'D:/result.txt'
    similarity = calculate_similarity(file1, file2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test3():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_1.txt'
    result = 'D:/result.txt'
    similarity = calculate_similarity(file1, file2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test4():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_10.txt'
    result = 'D:/result.txt'
    similarity = calculate_similarity(file1, file2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test5():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_15.txt'
    result = 'D:/result.txt'
    similarity = calculate_similarity(file1, file2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def main():
   test1()
   test2()
   test3()
   test4()
   test5()

if __name__ == '__main__':
  main()






