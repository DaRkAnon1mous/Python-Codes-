def get_key(name):
    registration = {
        'John': 'A011',
        'Kyle': 'A009',
        'Jake': 'BQ02',
        'Tamra': 'A015',
        'Josh': 'BQ13'
    }
    
    if name in registration:
        print("Key :", registration[name])
    else:
        print("Not Registered")

guest_1 = 'jake'
guest_2 = 'tamra'
guest_3 = 'Ted'

get_key(guest_1)
get_key(guest_2)
get_key(guest_3)
