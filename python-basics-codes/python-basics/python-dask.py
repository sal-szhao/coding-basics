import os
import time
import pandas as pd
import numpy as np
import dask.dataframe as dd
import dask.array as da


'''
Dask will creast a task graph first.
Actual computing will be accomplished when necessary.
'''
ddf = dd.read_csv(
    os.path.join("nycflights", "*.csv"), parse_dates={"Date": [0, 1, 2]}
)

# print(ddf.visualize())    # Generate the task graph.
print(len(ddf))

'''
Compare speed of pandas and dask.
'''

begin = time.time()
files = os.listdir(os.path.join('nycflights'))
pdf = pd.DataFrame()
for file in files:
    pdf = pd.concat([pdf, pd.read_csv(os.path.join('nycflights', file))], axis=0)
print(len(pdf))
end = time.time()
print("pandas time: ", end - begin)

begin = time.time()
ddf = dd.read_csv(
    os.path.join("nycflights", "*.csv"), parse_dates={"Date": [0, 1, 2]}
)
print(len(ddf))
end = time.time()
print("dask time: ", end - begin)

'''
Compare speed of numpy and dask.
'''

begin = time.time()
xn = np.random.normal(10, 0.1, size=(30_000, 30_000))
print(xn.mean(axis=0))
end = time.time()
print("numpy time: ", end - begin)

begin = time.time()
xd = da.random.normal(10, 0.1, size=(30_000, 30_000), chunks=(3000, 3000))
print(xd.mean(axis=0).compute())
end = time.time()
print("dask time: ", end - begin)
