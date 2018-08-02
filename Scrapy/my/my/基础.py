import scrapy
from scrapy import Field, Selector

s={'name': '更多产品', 'url': ['//www.baidu.com/more/']}
print(s['name'])
print(s['url'])
s['s']='aaaa'
print(s)

k=Field()



class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
product = Product(name='Desktop PC', price=1000)
print (product)
print(product['name'])
print(product.get('name'))
print(product['price'])
print(product.get('last_updated', 'not set'))
print( product.get('lala', 'unknown field'))
print('name' in product)
print('last_updated' in product)
print('last_updated' in product.fields)
print('lala' in product.fields )


# 选择器
body = '<html>' \
       '<body>' \
       '<span>good</span>' \
       '</body></html>'
print(Selector(text=body).xpath('//span').extract())

sel = Selector(text="""
    <ul class="list">
         <li>1</li>
         <li>2</li>
         <li>3</li>
     </ul>
     <ul class="list">
         <li>4</li>
         <li>5</li>
         <li>6</li>
     </ul>""")
xp = lambda x: sel.xpath(x).extract()
print(xp("//li[1]"))
print(xp("(//li)[1]"))
print(xp("//ul/li[1]"))
print(xp("(//ul/li)[1]"))