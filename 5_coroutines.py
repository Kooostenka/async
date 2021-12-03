def coroutine(func): #инициализация генератора
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready'
    message = yield x
    print(message)

class OkException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ =0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration: #throw
            print("Done")
        except OkException:
            print('..................../')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average
