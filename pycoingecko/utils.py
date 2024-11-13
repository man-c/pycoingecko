from functools import wraps


def func_args_preprocessing(func):
    """Return function that converts list input arguments to comma-separated strings"""

    @wraps(func)
    def input_args(*args, **kwargs):

        # check in **kwargs for lists and booleans
        for v in kwargs:
            kwargs[v] = arg_preprocessing(kwargs[v])
        # check in *args for lists and booleans
        args = [arg_preprocessing(v) for v in args]

        return func(*args, **kwargs)

    return input_args


def arg_preprocessing(arg_v):
    """Return the values of an argument after preprocessing"""

    # check if arg is list and convert it to comma-separated string
    if isinstance(arg_v, list):
        arg_v = ','.join(arg_v)
    # check if arg is boolean and convert it to string
    elif isinstance(arg_v, bool):
        arg_v = str(arg_v).lower()

    return arg_v


def get_comma_separated_values(values):
    """Return the values as a comma-separated string"""

    # Make sure values is a list or tuple
    if not isinstance(values, list) and not isinstance(values, tuple):
        values = [values]

    return ','.join(values)

