import csv
import re


def extractRows(reader):
    ret = []
    for index, row in enumerate(reader):
      # if index > 40:
      #     break
      row['year'] = row['date'][0:4]
      ret.append(row)
    return ret


def groupBy(key, commentArr):
    ret = {}

    for row in commentArr:
        if row[key] not in ret.keys():
            ret[row[key]] = []
        ret[row[key]].append(row)
    return ret


def calcAvgScore(rows):
  ret = {}
  for key in rows[0].keys():
    total = 0
    count = 0
    avg = 0
    for row in rows:
      if re.search('[\u4e00-\u9fa5]', key):
        if row[key] != 'nan':
          total = total + float(row[key])
          count = count + 1
    if count == 0:
      avg = 'nan'
    else:
        avg = round(total / count, 2)
    if re.search('[\u4e00-\u9fa5]', key):
      ret[key] = avg
    else:
      ret[key] = row[key]
  return ret


def writeCSV(comments):
  f = open('avgCredit.csv', 'w', encoding='utf-8', newline='')
  csv_writer = csv.writer(f)
  csv_writer.writerow(comments[0].keys())
  rows = []
  for obj in comments:
      valueList = []
      for key in obj.keys():
          valueList.append(obj[key])
      rows.append(valueList)
  csv_writer.writerows(rows)
  f.close()
  return


with open('withCredit.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = extractRows(reader)
    grouped = groupBy('listing_id', rows)
    result = []
    f = []
    for rooms in grouped.values():
      groupedByYear = groupBy('year', rooms)
      for rowsInSameYear in groupedByYear.values():
        avg = calcAvgScore(rowsInSameYear)
        avg["count"] = len(rowsInSameYear)
        result.append(avg)
    groupedTmpResult = groupBy('listing_id', result)
    for item in groupedTmpResult:
      room = groupedTmpResult[item]
      for comment in room:
        nextYearComment = list(filter(lambda x: x['year']
                                      == str(int(comment['year']) + 1), room))
        if len(nextYearComment) == 1:
          comment['count + 1'] = nextYearComment[0]['count']
        else:
          comment['count + 1'] = 0
        f.append(comment)

    writeCSV(f)
