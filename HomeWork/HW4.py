# Задание 1
def check_type(funs):
    def wrapper(arg):
        if type(arg) in (int, float):
            return funs(arg)
        else:
            print('Ошибка: ожидалось число')
    return wrapper


@check_type
def square(x):
    return x * x

print(square(4))  # 16
print(square("hi")) # Ошибка: ожидалось число


# Задание 2

def count_calls(func):
    def wrapper(*num1, **num2):
        wrapper.calls += 1
        print(f"Функция вызвана {wrapper.calls} раз")
        return func(*num1, **num2)
    wrapper.calls = 0
    return wrapper

@count_calls
def hello():
    print("Привет")

hello()
hello()
hello()