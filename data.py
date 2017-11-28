import numpy as np
import pandas as pd

a = np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3]])
print(a)

df =pd.DataFrame(a)
print(df)

b = np.array([1,2,3,4])
print(b)

sr = pd.Series(b)
print(sr)

c = np.random.random((2,4,5))
print(c)

pn = pd.Panel(c)
print(pn)



print("Indexing.......")
index = a[0:2,1:3]
print(index)

print(a[1, :])
print(a[1:2, :])
