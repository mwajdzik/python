import pandas

print(pandas.eval('2 + 3'))
print(pandas.eval('2 + pi', local_dict={'pi': 3.14}))
print(pandas.eval('True and False or cond', local_dict={'cond': True}))
