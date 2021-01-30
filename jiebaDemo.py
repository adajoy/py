import jieba
import csv

def getComments(reader):
    comments = []
    for index, row in enumerate(reader):
        comment = row['comments']
        comments.append(comment)
    return comments

def splitComments(comments):
    words = {}
    for comment in comments:
        seg_list = jieba.cut(comment)
        for word in seg_list:
            if word == '\r\n':
                continue
            if word not in words.keys():
                words[word] = {}
                words[word]['count'] = 1
            words[word]['count'] += 1
    return words

def orderWords(words):
    arr = []
    for item in words.items():
        arr.append((item[0],item[1]['count']))
    return sorted(arr, key=lambda x:x[1], reverse=True)

with open('filtered.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    allComments = getComments(reader)
    words = splitComments(allComments)
    orderedWords = orderWords(words)
    
    f = open('count.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['word', 'count'])
    for item in orderedWords:
        if (item[0] is not None) & (item[1] is not None):
            csv_writer.writerow([item[0], str(item[1])])
    f.close()