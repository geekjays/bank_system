import functools

def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        account = args[0]
        operation_name = func.__name__.replace('_', ' ').capitalize()
        print(f"Operation: {operation_name} | Account: {account.name} | Balance: {account.balance}")
        return result
    return wrapper
