import functools

def repeat(*args, **kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*f_args, **f_kwargs):
            times = kwargs.get('times', 1)
            for _ in range(times):
                func(*f_args, **f_kwargs)
        return wrapper

    # Nếu gọi như @repeat(3) hoặc @repeat(times=3)
    if args and callable(args[0]):
        # Trường hợp dùng @repeat (không có tham số)
        return decorator(args[0])
    else:
        # Trường hợp dùng @repeat(3) hay @repeat(times=3)
        if args:
            kwargs['times'] = args[0]
        return decorator


@repeat
def hello1():
    print("hello1")

@repeat(3)
def hello2():
    print("hello2")

@repeat(times=2)
def hello3():
    print("hello3")

hello1()
hello2()
hello3()
