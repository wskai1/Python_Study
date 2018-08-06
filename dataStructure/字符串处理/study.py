import html
import re
import textwrap

line = 'asdf fjdk; afed, fjek,asdf, foo'
s=re.split(r'[;,\s]\s*', line)
print(s)

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

filename = 'spam.txt'
print(filename.endswith('.txt'))
filename.startswith('file:')
url = 'http://www.python.org'
print(url.startswith('http:'))

url = 'http://www.python.org'
s=re.match('http:|https:|ftp:', url)
print(s)

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

# 匹配日期
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print("yyyyy")
else:
    print("nnnn")
if re.match(r'\d+/\d+/\d+', text2):
 print("yyyyy")
else:
    print("nnnn")

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
print("=====================")
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
print(month)
print(day)
print(year)
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# 字符串的搜索和替换
text = 'yeah, but no, but yeah, but no, but yeah'
text1=text.replace('yeah','mmmmm')
print(text)
print(text1)

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text1=re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
text2=text.replace('/','-')
print(text)
print(text1)
print(text2)

# 多次替换 考虑性能
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)

# 忽略大小写
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
str=re.compile(r'"(.*?)"')
print(str.findall(text2))

# 多行匹配
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''
print(comment.findall(text1))
print(comment.findall(text2)) #不能匹配到换行符号
# 支持换行匹配的几种方法
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))

# Unicode标准化
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1==s2)
print(len(s1))
print(len(s2))

# 删除
# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

s = ' hello     world \n'
print(s.strip())
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))

# 字符串对齐
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20,'='))
print(text.center(20,'*'))
# 利用format对齐
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>15s'))
print(format(text, '=<15s'))
print(format(text, '*^15s'))

print('{:>10s} {:>10s}'.format('Hello', 'World'))
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

# 合并拼接字符串
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))
print('==='.join(parts))
data = ['ACME', '50', '91.1']
print(','.join(data for data in data))

a='147'
b='369'
c='258'
print(a, b, c, sep=' ') # Better
s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))


s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s, 10))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))

# 处理HTML和XML
s = 'Elements are written as "<tag>text</tag>".'
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))