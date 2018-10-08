def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(a_list):
    a_list = [int(x) for x in a_list]
    a_list = [x for x in a_list if x%2 == 0]
    a = sum(a_list)
    return a


# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
