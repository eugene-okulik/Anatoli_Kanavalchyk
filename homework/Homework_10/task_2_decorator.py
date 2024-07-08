from functools import wraps


def repeat_me(func):
    @wraps(func)
    def wrapper(text, count=1):
        for _ in range(count):
            func(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
