# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv
filename = 'diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

# Histogram
data.hist()

# Density plot (distribution of each attribute)
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()

# box and whisker plots (review the distribution of each attribute)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.figure()
pyplot.show()
