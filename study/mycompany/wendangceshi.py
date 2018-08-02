# coding:UTF-8
import doctest

def ceshi(x):
    """#这是文档测试的内容
    >>> ceshi(2)
    1
    >>> ceshi(3)
    0
    >>> ceshi(4)
    0
    """  # End
    if x % 2 == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    doctest.testmod(verbose=True)  # doctest.testmod是测试模块，verbose默认是False,意思是出错才用提示；True，对错都有执行结果
