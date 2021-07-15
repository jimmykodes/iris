#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from sklearn.cluster import KMeans

resp = requests.get("http://localhost:5000")
soup = BeautifulSoup(resp.content, features="html.parser")

x_train = []
x_test = []
y_train = []

for el in soup.find(id="training-data").find_all('li'):
    x = [0, 0, 0, 0]
    y = 0
    for k, v in el.attrs.items():
        if k == 'data-0':
            x[0] = float(v)
        if k == 'data-1':
            x[1] = float(v)
        if k == 'data-2':
            x[2] = float(v)
        if k == 'data-3':
            x[3] = float(v)
        if k == 'data-y':
            y = int(y)
    x_train.append(x)
    y_train.append(y)

for el in soup.find(id="testing-data").find_all('li'):
    x = [0, 0, 0, 0]
    for k, v in el.attrs.items():
        if k == 'data-0':
            x[0] = float(v)
        if k == 'data-1':
            x[1] = float(v)
        if k == 'data-2':
            x[2] = float(v)
        if k == 'data-3':
            x[3] = float(v)
    x_test.append(x)

k = KMeans(n_clusters=3).fit(x_train, y_train)
y_test = k.predict(x_test)
resp = requests.post("http://localhost:5000/test", json=[int(y) for y in y_test])
print(resp.json())
