# Python3 对敏感词汇的过滤

__all__ = [ 'BSFilter'， 'DFAFilter'， 'NaiveFilter' ]

__author__ = 'tao'

__date__ = '2021.12.05'

> BSFilter
  直接过滤敏感词汇， 所有字符统用一个 * 表示

> DFAFilter
  直接过滤敏感词汇， 每个字符都是用一个 * 表示

> NaiveFilter
  调用文件keywords中的敏感词汇来过滤， 所有字符只用一个 * 表示
