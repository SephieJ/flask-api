# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import glob

folder = 'temp_aiml/'
for filename in glob.glob(os.path.join(folder, '*.aiml')):
    print(filename)
    with open(filename, 'r') as myfile:
        soup = BeautifulSoup(myfile.read(), 'html.parser')
    data = []
    for cat in soup.find_all('category'):
        if cat.parent.name == "topic":
            continue
        data += [cat.find("pattern").text]
    print(data)
    data_set = " ".join(data)
    # print(data_set)
