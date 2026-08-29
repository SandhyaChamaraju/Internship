class Sample:
    # Replacing 'self' with custom variable names
    def __init__(harry, name):
        harry.name = name

    def greet(slf):
        print(f"Hello, {slf.name}!")

# Testing the custom parameter names
obj = Sample("Harry")
obj.greet()
