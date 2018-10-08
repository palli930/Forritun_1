def safe_input(prompt,type):
    val1 = input('Please enter an integer: ')
    try:
        val1 = int(type)
    except ValueError:
        print("Error: please enter a value of ", a_type)
    return x

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))
