import csv
import re
import time


def chineseFilter(reader):
    ret = []
    for row in reader:
        res = re.search('[\u4e00-\u9fa5]', row['comments'])
        if res:
            ret.append(row)
    return ret


def groupBy(key, commentArr):
    ret = {}

    for row in commentArr:
        if row[key] not in ret.keys():
            ret[row[key]] = []
        ret[row[key]].append(row)
    return ret


def moreThanFilter(dict, amount):
    ret = {}
    for key in dict.keys():
        items = dict[key]
        count = len(items)
        if count > amount:
            ret[key] = items

    return ret


def filter(arr, filterFn):
    filtered = []
    for item in arr:
        if filterFn(item):
            filtered.append(item)
    return filtered


def laterThan2016(item):
    timestamp2016 = time.mktime(time.strptime('2016-1-1', '%Y-%m-%d'))
    commentTime = time.mktime(time.strptime(item['date'], '%Y/%m/%d'))
    return commentTime >= timestamp2016


def latestFilter(dict):
    ret = {}
    for key in dict.keys():
        items = dict[key]
        items = filter(items, laterThan2016)
        if len(items) > 0:
            ret[key] = items
    return ret


def unwarpComments(dict):
    ret = []
    for key in dict.keys():
        items = dict[key]
        for item in items:
            ret.append(item)
    return ret


def writeCSV(comments):
    f = open('filtered.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['listing_id', 'location', 'date', 'comments'])
    rows = []
    for obj in comments:
        valueList = []
        for key in obj.keys():
            valueList.append(obj[key])
        rows.append(valueList)
    csv_writer.writerows(rows)
    print(len(rows))
    f.close()
    return


with open('reviews_detail.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    chs = chineseFilter(reader)
    grouped = groupBy('listing_id', chs)
    moreThan5 = moreThanFilter(grouped, 5)
    # latest = latestFilter(moreThan5)
    latest = moreThan5
    comments = unwarpComments(latest)
    writeCSV(comments)
