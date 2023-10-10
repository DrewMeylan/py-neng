def logger(func):
    import logging
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args}, and kwargs: {kwargs} '
        )
        return func(*args, **kwargs)
    
    return wrapper

def my_timer(func):
    import my_timer
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{func.__name__} executed in {t2} seconds')
        return result
    return wrapper

    