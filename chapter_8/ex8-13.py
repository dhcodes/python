def build_profile(first, last, **user_info):
    #create a user profile for a new person
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('d','h',location='us',field='programming',cats=2)
print(user_profile)
