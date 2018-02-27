# pima indians diabetes
from pandas import read_csv
from pandas import set_option
filename = "diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

# View first 20 rows
peek = data.head(20)
print(peek)
# dimensions of data
shape = data.shape
print(shape)

# data types for each attribute
types = data.dtypes
print(types)

# statistical summary
set_option('display.width', 100)
set_option('precision', 3)
description = data.describe()
print(description)

# class distribution
class_counts = data.groupby('class').size()
print(class_counts)

#pairwise pearson correlations
correlations = data.corr(method='pearson')
print(correlations)

# skew (refers to a distribution that is assumed Gaussian that is shifted or squashed in one direction or another)
skew = data.skew()
print(skew)
