import jieba
import csv

def split(sentence):
  seg_list = jieba.cut(sentence)
  s = ''
  for word in seg_list:
    s = s + word + '/'
  return s + '\n'

def getComments(reader):
    comments = []
    for index, row in enumerate(reader):
        comment = row['comments']
        comments.append(comment)
    return comments

with open('reviews_detail.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    allComments = getComments(reader)
    f = open('split.txt', 'w', encoding='utf-8', newline='')
    for comment in allComments:
      s = split(comment)
      f.write(s)
    f.close()