# 2. Nested Dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print(ramit["email"])

print(ramit["interests"][0])

print(ramit["friends"][0]["email"])

print(ramit["friends"][1]["interests"][1])

# 3. Friend Counter

def count_friends(contact_dict):
    friend_counter = 0
    for count in contact_dict["friends"]:
        friend_counter += 1
    
    contact_dict["friend_count"] = friend_counter
    return contact_dict

print(count_friends(ramit))