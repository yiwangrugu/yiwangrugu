import jieba
import difflib
from collections import Counter
from math import sqrt


def cos_similarity(text1, text2):
    # 长文本相似度比较
    # 读取文本文件

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
    # 短文本相似度比较
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
    similarity = cos_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test2():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_del.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity = cos_similarity(text1, text2)
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
    similarity = cos_similarity(text1, text2)
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
    similarity = cos_similarity(text1, text2)
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
    similarity = cos_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test6():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "这是一句话，一句没意义的话，可以用作测试，验证可行性。 "
    result = 'D:/result.txt'
    similarity = cos_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test7():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "这是一句话，一句有意义的话，用作测试验证此程序的可行性。 "
    result = 'D:/result.txt'
    similarity = cos_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))


def test8():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "一二三四五六七，数来数去数不清。 "
    result = 'D:/result.txt'
    similarity = cos_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test9():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "这是一句抄袭的话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    result = 'D:/result.txt'
    similarity = cos_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test10():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_add.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity = diff_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test11():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_del.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity = diff_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test12():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_1.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity = diff_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test13():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_10.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity = diff_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test14():
    file1 = 'D:\测试文本\orig.txt'
    file2 = 'D:\测试文本\orig_0.8_dis_15.txt'
    result = 'D:/result.txt'
    with open(file1, 'r', encoding='utf-8') as f:
        text1 = f.read()
    with open(file2, 'r', encoding='utf-8') as f:
        text2 = f.read()
    similarity = diff_similarity(text1, text2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test15():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "这是一句话，一句没意义的话，可以用作测试，验证可行性。 "
    result = 'D:/result.txt'
    similarity = diff_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test16():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "这是一句话，一句有意义的话，用作测试验证此程序的可行性。 "
    result = 'D:/result.txt'
    similarity = diff_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))


def test17():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "一二三四五六七，数来数去数不清。 "
    result = 'D:/result.txt'
    similarity = diff_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))

def test18():
    test1 = "这是一句话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    test2 = "这是一句抄袭的话，一句没什么意义的话，但是可以用作测试，验证此程序的可行性。 "
    result = 'D:/result.txt'
    similarity = diff_similarity(test1, test2)
    with open(result, 'a') as f:
        f.write('相似度：{:.2f}\n'.format(similarity))


def main():
   with open('D:/result.txt', 'w') as f:
       f.write("余弦相似度比较法：\n")
       f.close
   test1()
   test2()
   test3()
   test4()
   test5()
   test6()
   test7()
   test8()
   test9()
   with open('D:/result.txt', 'a') as f:
       f.write("difflib库比较法：\n")
       f.close
   test10()
   test11()
   test12()
   test13()
   test14()
   test15()
   test16()
   test17()
   test18()

if __name__ == '__main__':
  main()






