import os
import time
import pandas as pd
import numpy as np
import dask.dataframe as dd
import dask.array as da


'''
Dask will creast a task graph first.
Actual computing will be accomplished when necessary (scheduler).
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


'''
Dask can also be used in a more general scenario 
by using the `delayed` function for parallel computing.
'''
import dask 

begin = time.time()

def inc(x):
    time.sleep(1)
    return x + 1

def double(x):
    time.sleep(1)
    return x * 2

def add(x, y):
    time.sleep(1)
    return x + y

data = [1, 2, 3, 4, 5]

output = []
for x in data:
    a = inc(x)
    b = double(x)
    c = add(a, b)
    output.append(c)

total = sum(output)

end = time.time()
print("normal time: ", end - begin)


begin = time.time()

@dask.delayed
def inc(x):
    time.sleep(5)
    return x + 1

@dask.delayed
def double(x):
    time.sleep(5)
    return x * 2

@dask.delayed
def add(x, y):
    time.sleep(5)
    return x + y

data = [1, 2, 3, 4, 5]

output = []
for x in data:
    a = inc(x)
    b = double(x)
    c = add(a, b)
    output.append(c)

total = dask.delayed(sum)(output)

end = time.time()
print("delayed time: ", end - begin)
