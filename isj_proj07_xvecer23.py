#!/usr/bin/env python3


class TooManyCallsError(Exception):
    ''' Define specific exception for calling a function too many times. '''
    def __init__(self, msg):
        ''' Call the base class constructor with the parameters it needs. '''
        super(TooManyCallsError, self).__init__(msg)


def limit_calls(max_calls = 2, error_message_tail = 'called too often'):
    ''' Function decorator to prevent functions from being called too often. '''
    def decorator(func):
        ''' Decorator. '''
        func.var = 0
        
        def wrapper(*args, **kwargs):
            ''' Wrapper. '''
            func.var += 1
            if func.var > max_calls:
                raise TooManyCallsError('function "' + func.__name__ + '" - '
                                        + error_message_tail)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def ordered_merge(*args, **kwargs):
    ''' Iterate over iterable objects in order set by selector. '''

    selector = kwargs.get('selector', [])
    if selector is None:
        return None

    args = list(args)
    ordered_lst = []

    for arg in range(len(args)):
        args[arg] = iter(args[arg])

    for item in selector:
        ordered_lst.append(next(args[item]))

    return ordered_lst


class Log():
    ''' Class for file output. '''
    def __init__(self, file):
        ''' Open file. '''
        self.file = open(file, 'w')

    def __enter__(self):
        ''' Begin writing to file. '''
        self.file.write("Begin\n")
        return self

    def logging(self, msg):
        ''' Write specified message to log file. '''
        self.file.write(msg + "\n")

    def __exit__(self, exc_type, exc_value, traceback):
        ''' End file writing. '''
        self.file.write("End\n")
        self.file.close()
