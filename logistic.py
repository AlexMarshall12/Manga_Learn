from xml.dom import minidom
import numpy as np

from matplotlib.colors import hex2color
import csv
from svg.path import parse_path

with open('sabody.svg','rb') as svg_file:
    with open('res.txt','wb') as res_file:
        doc = minidom.parse(svg_file)  # parseString also exists
        paths = []
        for path in doc.getElementsByTagName('path'):
            fill = path.getAttribute('fill')
            res_file.write(fill+'\n')
            d = path.getAttribute('d')
            paths.append(d)
    doc.unlink()

#print (path_strings)

CURVE_DIVS = 50.0000000

for i,path in enumerate(paths):
    P = parse_path(path)
    length = P.length()
    corners = []
    for item in xrange(int(CURVE_DIVS)):
        dist = item/CURVE_DIVS
        print dist
        each_point = P.point(dist)
        x = each_point.real
        y = each_point.imag
        corners.append((x,y))
    n = len(corners) # of corners
    area = 0.0
    print corners
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    index = i
    complexity = len(path)
    lines = path.count('L')
    curves = path.count('C')
    rgb = hex2color("#ff0000")
    intensity =  0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    writer.writerow([area,length,index,complexity,lines,curves,intensity])
