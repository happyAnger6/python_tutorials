__author__ = 'zhangxa'

"""
从多个选择分支中匹配完整的单词
如果不用\b表示完整的单词，正则表达式将会在匹配到第一个满足条件的选择分支后就停止
"""
import re

if __name__ == "__main__":
    rec = re.compile('\\bJane\\b|\\bJanet\\b')
    rec1 = re.compile('Jane|Janet')
    print(rec.search('He went to Janet home'))
    print(rec.search('He went to Jane home'))
    print(rec1.search('He went to Janet home'))
    print(rec1.search('He went to Jane home'))