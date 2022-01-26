# array filter

print('####array filter')

arr = ['a', 'b', 'c']

def match(i):
  return i != 'b'

# def filter(arr, filterFn):
#   filtered = []
#   for item in arr:
#     if filterFn(item):
#       filtered.append(item)
#   return filtered

# print(filter(arr, match))

print(list(map(lambda item: item + 'c' ,filter(match, arr))))


## define function

print('####define function')

def add(a, b):
  return a + b

print(add(1, 2))

range(10)

## include

arr = ['房东', '房间', '房子', '非常', '特别', '超级', '北京', '不错', '推荐', '真的', '下次', '感觉']
append = ['方便', '干净']
a = 1
print(a not in arr)
arr.extend(append)
print(arr)

commonExclude = ['房东', '房间', '房子', '非常', '特别',
                 '超级', '北京', '不错', '推荐', '真的', '下次', '感觉']
specialExclude = ['方便', '干净']
w = commonExclude.extend(specialExclude)
print(w)
