import os
import csv
import re
from PIL import Image

if not os.path.exists('output'):
    os.makedirs('output')

with open('export.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        filename = 'input/' + line['image']
        im = Image.open(filename)
        w, h = im.width, im.height
        l = float(line['xmin'])
        t = float(line['ymin'])
        r = float(line['xmax'])
        b = float(line['ymax'])
        # Crop and save
        im = im.crop((l,t,r,b))
        filename = filename[5:]
        im.save("output/" + filename)

    

