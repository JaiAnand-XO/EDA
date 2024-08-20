import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = ['aa','2024-08-18',100,92]

#create SERIES using the given data
s1 = pd.Series(h)
print(s1)

#create INDEX for the given data
s2 = pd.Series(h,index = ['name','date','shares','value'])
print(s2)

#Obtain particular row
print(s2["name"])

