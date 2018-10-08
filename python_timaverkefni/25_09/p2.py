
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
for i in the_string:
    if ',' in the_string:
        to_list = the_string.split(',')
    else:
        to_list = the_string.split(' ')


print(to_list)