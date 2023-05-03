data = ("self", "py", 1.543)
format_string = "Hello"
format_string += " {}.{} learner, you have only {:.2} units left before you master the course!".format(*data)
print(format_string)
