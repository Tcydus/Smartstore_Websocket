import asyncio

@asyncio.coroutine
def func_normal():
    print('A')
    yield from asyncio.sleep(5)
    print('B')
    return 'saad'

@asyncio.coroutine
def func_infinite():
    while True:
        for i in range(10):
            print("--%d" % i)
            return 'saad'+str(i)

    
@asyncio.coroutine
def func_2():
  # while True :
  print("func_2")
    

loop = asyncio.get_event_loop()
tasks = [func_normal(), func_infinite()]
a, b  = loop.run_until_complete(asyncio.gather(*tasks))
c = loop.run_until_complete(func_2())
print("func_normal()={a}, func_infinite()={b} ,func_infinite={c}".format(**vars()))
print(b)
# loop.close()