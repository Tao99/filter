#!/usr/bin/env python3.7
# -*- coding:utf-8 -*-

from collections import defaultdict
import re


class BSFilter:
    """
    直接过滤敏感词汇, 所有字符统用一个 * 代表
    Filter Messages from keywords
    Use Back Sorted Mapping to reduce replacement times
    >>> f = BSFilter()
    >>> f.add("sexy")
    >>> f.filter("hello sexy baby")
    hello * baby
    """
    def __init__(self):
        self.keywords = []
        self.kw_sets = set([])
        self.bs_dict = defaultdict(set)
        self.pat_en = re.compile(r'^[0-9a-zA-Z]+$')  # English phrase or not

    def add(self, keyword):
        if not isinstance(keyword, str):
            keyword = keyword.decode('utf-8')
        keyword = keyword.lower()
        if keyword not in self.kw_sets:
            self.keywords.append(keyword)
            self.kw_sets.add(keyword)
            index = len(self.keywords) - 1
            for word in keyword.split():
                if self.pat_en.search(word):
                    self.bs_dict[word].add(index)
                else:
                    for char in word:
                        self.bs_dict[char].add(index)

    def parse(self, path):
        with open(path, "r") as f:
            for keyword in f:
                self.add(keyword.strip())

    def filter(self, message, replace="*"):
        """
        :param message: 需要过滤敏感词汇的语句
        :param replace: 不填默认用 * 表示，可以自定义
        :return: 过滤后的语句
        """
        if not isinstance(message, str):
            message = message.decode('utf-8')
        message = message.lower()
        for word in message.split():
            if self.pat_en.search(word):
                for index in self.bs_dict[word]:
                    message = message.replace(self.keywords[index], replace)
            else:
                for char in word:
                    for index in self.bs_dict[char]:
                        message = message.replace(self.keywords[index], replace)
        return message


if __name__ == '__main__':
    file = BSFilter()
    file.add("sexy")
    print(file.filter("hello sexy baby", "--"))
