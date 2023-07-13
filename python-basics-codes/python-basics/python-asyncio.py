import asyncio


'''
Directly call the async function will return a coroutine object.
Use `asyncio.run` to create an event loop and add async function to it.
Asyncio will always run in a single thread.
'''
async def foo(text):
    print(text)

print(foo('text'))  
asyncio.run(foo('text'))

print("-" * 65)


'''
`asyncio.sleep` itself is an async function.
`create_task` will add the task to run in the background asap,
but will not execute immediately.
'''
async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    # await task        # await the task to be finished before continuing the main.
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())

print("-" * 65)


'''
asyncio will switch between `await`.
'''

async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(1)
    print('finished main')

async def foo(text):
    print(text)
    await asyncio.sleep(1)      # If sleep for too long, `main` will not wait for `foo` to finish.
    print('finished foo')   

asyncio.run(main())

print("-" * 65)


'''
Multiple tasks and await for all tasks to finish (Task is subclass of Future).
'''

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("finish fetching")
    return {"data": 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    data = await task1
    print(data)
    await task2

asyncio.run(main())

print("-" * 65)

'''
create_task can only create one task at a time.
asyncio.gather can create multiple tasks at a time.
'''
async def main():
    task1 = fetch_data()
    task2 = print_numbers()
    data, _ = await asyncio.gather(task1, task2)
    print(data)

asyncio.run(main())