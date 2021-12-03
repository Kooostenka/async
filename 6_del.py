def coroutine(func): #инициализация генератора
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class OkException(Exception):
    pass


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('Hello!')
            break
        else:
            print('.....', message)
    return 'Returned from subgen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except OkException as e:
    #         g.throw(e)
    result = yield from g
    print(result)