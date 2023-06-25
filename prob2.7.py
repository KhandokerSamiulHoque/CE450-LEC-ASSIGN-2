def smth(g, dx):
    try:
        return lambda x: (g(x - dx) + g(x) + g(x + dx)) / 3
    except Exception as error:
        return lambda x: f"Error: {error}"


try:
    g_val = input("Enter the function square =  ")
    g = eval(g_val)
    dx = float(input("Enter the value of dx: "))
    
    if not callable(g):
        raise ValueError("Error!! input the correct function")

    smth_g = smth(g, dx)  

    
    x = float(input("Enter a value for x: "))  
    result = smth_g(x)  

    if isinstance(result, str):  
        print(result)  
    else:
        print(round(result, 3))  
except Exception as error:
    print(f"Error: {error}")
