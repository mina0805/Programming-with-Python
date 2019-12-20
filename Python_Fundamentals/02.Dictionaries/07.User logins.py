raw_data = input()

login_dict = {}
unsuccessful_logins = 0

while raw_data != 'login':
    login, password = raw_data.split('->')
    for i in raw_data:
        if i != " ":
            login_dict[login] = password
    raw_data = input()

raw_data = input()

while raw_data != 'end':
    login, password = raw_data.split('->')
    print(login, password)
    #if login_dict.get(login) == password:
        print(f'{login}: logged in successfully')
    else:
        print(f'{login}: login failed')
        unsuccessful_logins += 1

    raw_data = input()

print("unsuccessful login attempts:", unsuccessful_logins)