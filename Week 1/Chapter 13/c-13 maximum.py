from functools import reduce
numbers=[10,25,7,45,98,32]

maximum=reduce(lambda a,b:a if a>b else b,numbers)
print("The maximum number is:",maximum)
