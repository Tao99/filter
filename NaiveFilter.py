#!/usr/bin/env python3.7
# -*- coding:utf-8 -*-





class NaiveFilter:
    """
    调用文件keywords中的敏感词汇来过滤，所有字符只用一个 * 代表
    Filter Messages from keywords
    very simple filter implementation
    >>> f = NaiveFilter()
    >>> f.parse("keywords")
    >>> f.filter("hello sexy baby")
    hello * baby
    """
    def __init__(self):
        self.keywords = set([])

    def parse(self, path):
        for keyword in open(path):
            self.keywords.add(keyword.strip().encode('utf-8').decode('utf-8').lower())

    def filter(self, message, replace="*"):
        """
        :param message: 需要过滤敏感词汇的语句
        :param replace: 不填默认用 * 表示，可以自定义
        :return: 过滤后的语句
        """
        message = str(message).lower()
        for kw in self.keywords:
            message = message.replace(kw, replace)
        return message


if __name__ == "__main__":
    file = NaiveFilter()
    file.parse("keywords")
    print(file.filter("hello sexy baby"))
