def f():
    return lambda: lambda x: lambda: x

result = f()()(3)()
print(result)