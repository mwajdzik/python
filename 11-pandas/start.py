import pandas as pd

x = pd.read_csv('./2017.csv')

print(x.index)
print(x.columns)
print(x.values)
print(x.shape)
print(x.size)
print(x.count())
print(x.describe())
print(x.head())
print(x.tail())

# to obtain the index label of the rows containing minimum and maximum values
y = x[['Happiness.Score', 'Freedom']]
print(y.idxmax())
print(y.idxmin())

# returns the number of times each value is repeated in the column
print(y['Freedom'].value_counts())
