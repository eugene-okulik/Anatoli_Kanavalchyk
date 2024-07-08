def finish_me(func):
    def wrapper(text):
        result = func(text)
        print("finished")
        return result

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
