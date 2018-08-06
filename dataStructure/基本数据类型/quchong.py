# 适用于hashable 类型
def quchong(items):
    set=[]
    for item in items:
        if item not in set:
           yield item
           set.append(item)
        else:
            continue
# 去除字典中重复的键值对

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == '__main__':
    items=[1,11,2,2,3,3,4,4,5,5,6,6,8,9,4,2,51,25,3]
    # 最简单方法：利用set，但是会改变列表原有的顺序
    print(set(items))
    # 方法二，利用上述函数可以维护列表顺序不被改变
    print(list(quchong(items)))