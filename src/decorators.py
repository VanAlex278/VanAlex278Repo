def log(filename=None):
    """Декоратор логирует работу функции и выводит результат в файл, или в консоль
     (если файл не указан)."""
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as error:
                log_message = f"{func.__name__} error: {error}. Inputs: {args, kwargs}."
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
            raise
        return wrapper
    return my_decorator
