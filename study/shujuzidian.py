#制造数据字典
import itertools as its
def dic():
    words = "1234568790abcdefghijkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ"
    r = its.product(words, repeat=8)
    dic = open("xiancheng1.txt", "a")
    for i in r:
        dic.write("".join(i))
        dic.write("".join("\n"))
    dic.close()
dic()