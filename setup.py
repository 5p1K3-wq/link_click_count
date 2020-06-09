token = input('Enter the access token to work with the service https://dev.bitly.com/index.html ')
with open('.env', 'w', encoding='utf-8') as file_env:
    file_env.write('ACCESS_TOKEN={}'.format(token))
print('Setup script completed successfully')