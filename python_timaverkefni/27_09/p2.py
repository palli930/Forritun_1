def list_to_tuple(a_list):
    for x in a_list:
        if x.isalpha():
            print("Error. Please enter only integers.")
            a_list = ()
            break
    a_list = [int(x) for x in a_list]
    return tuple(a_list)

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)