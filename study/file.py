from pip._vendor.distlib.compat import raw_input
#读文件
# f = open("w.txt", "r+", encoding='utf-8')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# while line:
#     print(line),  # 后面跟 ',' 将忽略换行符
#     # print(line, end = '')　　　# 在 Python 3中使用
#     line = f.readline()
#
# f.close()
#
#读文件
# from sys import argv
#
# script, filename = argv,'w.txt'
#
# txt = open(filename)
#
# print("Here's your file %r:" % filename)
# print (txt.read())
#
# print ("Type the filename again:")
# file_again = raw_input("> ")
#
# txt_again = open(file_again)
#
# print (txt_again.read())
#写文件
# from sys import argv
# script, filename = argv,'w1.txt'
# print ("Opening the file...")
# target = open(filename, 'w',encoding='utf-8')
#
# print ("Truncating the file.  Goodbye!")
# target.truncate()
# print( "Now I'm going to ask you for three lines.")
# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")
# print ("I'm going to write these to the file.")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# print ("And finally, we close it.")
# target.close()

#copy文件
from sys import argv
from os.path import exists

script, from_file, to_file = argv,'w.txt','w1.txt'
print("Copying from %s to %s" % (from_file, to_file))
# we could do these two on one line, how?
in_file = open(from_file,encoding='utf-8')
indata = in_file.read()
print ("The input file is %d bytes long" % len(indata))
print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")

out_file = open(to_file, 'w',encoding='utf-8')
out_file.write(indata)
print ("Alright, all done.")
out_file.close()
in_file.close()