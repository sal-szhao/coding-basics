from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

async def my_func_1():
    """
    my func 1
    """
    print('Func1 started..!!')
    await asyncio.sleep(5)
    print('Func1 ended..!!')

    return 'a..!!'

async def my_func_2():
    """
    my func 2
    """
    print('Func2 started..!!')
    await asyncio.sleep(5)
    print('Func2 ended..!!')

    return 'b..!!'

@app.get("/home-gather")
async def root():
    """
    my home route
    """
    start = time.time()
    futures = [my_func_1(), my_func_2()]
    a,b = await asyncio.gather(*futures)
    end = time.time()
    print('It took {} seconds to finish execution.'.format(round(end-start)))

    return {
        'a': a,
        'b': b
    }


# Will be directly running the following code.
@app.get("/home-create-task")
async def root():
    """
    my home route
    """
    start = time.time()
    asyncio.create_task(my_func_1())
    asyncio.create_task(my_func_2())
    end = time.time()
    print('It took {} seconds to finish execution.'.format(round(end-start)))

    return {
       'aaaa'
    }
