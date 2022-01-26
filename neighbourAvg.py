import csv
from geopy import distance
from openpyxl import Workbook
import copy
import re
wb = Workbook()


def calcNeighbourScore(rows, key):
  if len(rows) == 0:
    return 'nan'
  sum = 0
  for row in rows:
    sum += float(row[key])
  return sum / len(rows)


with open('neighbourAvg.csv', newline='', encoding='utf-8') as f:
  reader = csv.DictReader(f)
  arr = []
  dimensions = []
  for i, row in enumerate(reader):
    if i == 0:
        dimensions = list(filter(lambda x: re.search(
            '[\u4e00-\u9fa5]', x), row.keys()))
    # if i > 20:
    #   break
    arr.append(row)
  arr1 = copy.deepcopy(arr)

  for i, row in enumerate(arr):
    row['neighbour'] = []
    print(i)
    for j, row1 in enumerate(arr1):
        if i == j:
          continue
        coords_1 = (row['latitude'], row['longitude'])
        coords_2 = (row1['latitude'], row1['longitude'])
        d = distance.distance(coords_1, coords_2)
        if d < 0.5 and d > 0:
          row['neighbour'].append(copy.deepcopy(row1))

  for dimension in dimensions:
    ws = wb.create_sheet(dimension)
    ws.append(['listing_id', 'center_score', 'neighbor_score'])
    for i, row in enumerate(arr):
      ws.append([row['listing_id'], row[dimension],
                calcNeighbourScore(row['neighbour'], dimension)])
  wb.remove(wb.active)
  wb.save('wb.xlsx')
