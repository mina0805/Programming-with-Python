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
    if login_dict[user_name] == password:
        print(f'{user_name}: logged in successfully')
        raw_data = input()
    else:
        print(f'“{user_name}: login failed”. ')
        unsuccessful_logins += 1
        raw_data = input()

print(f'unsuccessful login attempts: {unsuccessful_logins}')
