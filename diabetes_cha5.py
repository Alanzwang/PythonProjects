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

# class distribution (how balanced the class values are)
class_counts = data.groupby('class').size()
print(class_counts)

# correlations (using Pearson's correlation coefficient)
# using corr() function on Pandas dataframe
correlations = data.corr(method='pearson')
print(correlations)

# skew (refers to a distribution that is assumed Gaussian that is shifted or squashed in one direction or another)
# an input attribute has a skew may allow you to perform data preparation to correct
# the skew and later improve the accuracy of the models.
# calculated using skew() function Pandas 
skew = data.skew()
print(skew)
