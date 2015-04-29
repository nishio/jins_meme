import csv
import numpy as np

data = []
for line in csv.reader(file('log.csv')):
    if len(line) < 2: continue
    if line[1] == 'test': continue
    if line[0] == '': continue
    data.append(list(map(float, line[1:])))

data = np.array(data)
labels = csv.reader(file('HEADER.csv')).next()

from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt

for i in [39, 40, 41, 42]:
    print labels[i]
    x = data[:, i]
    limmin = np.percentile(x, 0.1)
    limmax = np.percentile(x, 99.9)
    ls = np.linspace(limmin, limmax, 100)
    x = x[(x > limmin)&(x < limmax)]
    kde = gaussian_kde(x)
    plt.plot(ls, kde(ls), label=labels[i])

plt.xlim([limmin, limmax])
plt.legend()
plt.title('data distributions')
plt.show()
