from sys import argv

from pip._vendor.distlib.compat import raw_input

print("Hello Word!",end=" "),
print("I 'said' do not touch this.")
print("开始学习PYTHON")

text = "I am %d years old." % 22
print ("I said: %s." % text)
print ("I said: %r." % text)


# while True:
#     for i in ["/","-","|","\\","|"]:
#         print ("%s\r" % i),


age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print ("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))

