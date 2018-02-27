# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv
filename = 'diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
# data.hist()
#pyplot.show()

# density plots
# data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
# pyplot.show()

# box and whisker plots
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()
