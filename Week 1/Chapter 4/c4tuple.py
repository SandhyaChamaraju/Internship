my_tuple=(10,20,30)
try:
    my_tuple[1]=99
except TypeError as error:
    print(f"Error caught: {error}")
