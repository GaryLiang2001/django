name = input("please type your name > ")

adjectives = ['stupid ', 'scary ', 'interesting ', 'painful ', 'lazy ']
verbs = [' is glad to ', ' hate to ', " really want to ", " try best to "]
activities = ["sleep in class ", "wanna GPA plus ", "do something relaxing ", "dress up as a joker "]

import random
my_adjective = random.choice(adjectives)
my_verb = random.choice(verbs)
my_activity = random.choice(activities)

print(my_adjective + name + my_verb + my_activity)

