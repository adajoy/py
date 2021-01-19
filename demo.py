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