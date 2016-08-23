current_users = ['jad', 'ralphio', 'seal3', 'hoppy', 'pineappler']
new_users = ['steef', 'ralphio', 'hoppy', 'will16', 'rabidrabbit']

for user in new_users:
    if user.lower() in current_users:
        print("Name taken. Choose another.")
    else:
        print("Name is available.")
