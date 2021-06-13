from wordcloud import WordCloud
from os import path
import os
import csv

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
font_path = d + '/font/SourceHanSerifCN-Light.otf'

with open('count.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    dict = {}
    for row in reader:
      if len(row.get('word')) > 1:
        dict[row.get('word')] = int(row.get('count'))
    wc = WordCloud(font_path=font_path, width=1920, height=1080, background_color='white')
    wc.generate_from_frequencies(dict)
    wc.to_file(path.join(d, 'imgname1.jpg'))