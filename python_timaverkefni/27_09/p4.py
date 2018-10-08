def get_emails():
    user_input = input("Email address: ")
    email_list = [user_input]
    while user_input != 'q':
        if user_input == 'q':
            break
        user_input = input("Email address: ")
        email_list.append(user_input)
    email_list.pop()
    return email_list

def get_names_and_domains(email_list):
    names_and_domains = []
    for x in email_list:
        name,domain = x.split('@')
        tupla = (name,domain)
        names_and_domains.append(tupla)
    return names_and_domains


# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)
