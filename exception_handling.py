try:
    a = "hello"
    print(int(a))
except ValueError as e:
    print(f"that's not going to happen!, error: {e}")


# issubclass(ValueError, Exception)


class MyCustomException(Exception):
    pass


raise MyCustomException()


class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"got a bad value {value}"
        super().__init__(message)


my_value = 999
if my_value > 998:
    raise IncorrectValueError(my_value)
