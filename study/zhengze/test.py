import re

test = '用户输入的字符串'
if re.match(r'^', test):
    print('ok')
else:
    print('failed')

import re
text = input("Please input your Email address：\n")
if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
    print('Email address is Right!')
else:
    print('Please reset your right Email address!')