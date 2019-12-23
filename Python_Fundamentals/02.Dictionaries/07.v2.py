raw_data = input()

login_dict = {}
unsuccessful_logins = 0

while raw_data != 'login':
    user_name, password = raw_data.split('->')
    #for i in login, password:
        #if i != " ":
    login_dict[user_name] = password
    raw_data = input()

raw_data = input()

while raw_data != "end":
    user_name, password = raw_data.split('->')
    if user_name in login_dict:
        if login_dict[user_name] == password:
            print(f'{user_name}: logged in successfully')
        elif login_dict[user_name] != password:
            unsuccessful_logins += 1
            print(f'{user_name}: login failed. ')

        raw_data = input()

    else:
        print(login_dict.get(user_name,f'{user_name}: login failed. '))
        unsuccessful_logins += 1
        raw_data = input()

print(f'unsuccessful login attempts: {unsuccessful_logins}')
