import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'NAME' : ['JaiAnand','Akash','Akshaay'],
    'AGE' : [19,25,22],
    'SALARY' : [2000,5000,7500]
}

d = pd.DataFrame(data)
print(d)
