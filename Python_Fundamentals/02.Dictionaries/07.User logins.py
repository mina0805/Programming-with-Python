raw_data = input()

login_dict = {}
unsuccessful_logins = 0

while raw_data != 'login':
    login, password = raw_data.split('->')
    for i in login, password:
        if i != " ":
            login_dict[login] = password

while raw_data != "end":
    login, password = raw_data.split('->')
    for i in login, password:
        if i != " ":
            if login_dict[login] == password:
                print(f'{login}: logged in successfully')
            else:
                print(f'“{login}: login failed”. ')
                unsuccessful_logins +=1
                print(f'unsuccessful login attempts: {unsuccessful_logins}')
