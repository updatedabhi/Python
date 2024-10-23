'''
with open('./practice/poem.txt', 'r') as f:
  result = f.read()
  
print(f"This is your poem: \n {result}")

text = input("Enter text to find: ")

if text in result:
  print(f"Found '{text}' in the poem.")
else:
  print(f"'{text}' not found in the poem.")
  


import random
# print(random.random())

import random

# Function to generate a random score between 1 and 100
def play_generate_random_number_game():
    return random.randint(1, 100)

score = play_generate_random_number_game()
print(type(score))

# Open the score_card file and handle the score logic
with open('./practice/score_card.txt', 'r') as f:
    current_score = f.read()

# If the file is empty, write the current score
if current_score == '':
    with open('./practice/score_card.txt', 'w') as f:
        f.write(str(score))  # Convert score to string for writing
    print(f"First score recorded: {score}")
else:
    current_score = int(current_score)  # Convert the current score to an integer
    if current_score > score:
        print(f"Current high score {current_score} is greater than new score {score}.")
    else:
        with open('./practice/score_card.txt', 'w') as f:
            f.write(str(score))  # Write new high score as a string
        print(f"New high score: {score}")
        

with open('./practice/table/two_to_twenty.txt', 'a') as f:
    for i in range(2, 21):
        f.write(f"Table of {i}:\n") 
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")  
        f.write("\n") 
        

with open('./practice/abc.txt', 'r') as f:
    content = f.read()

if 'donkey' in content:
    content = content.replace('donkey', '$$$####')
    count += 1

with open('./practice/abc.txt', 'w') as f:
    f.write(content)
    


bad_words = ['madarchod', 'bhosriwala', 'bandar', 'randi']

with open('./practice/abc.txt', 'r') as f:
    content = f.read()

for bad_word in bad_words:
    content = content.replace(bad_word, '$$$####')

with open('./practice/abc.txt', 'w') as f:
    f.write(content)
    


with open('./practice/my_app.log', 'r') as f:
    log = f.read()
    
if 'python' in log.lower():
    print('Python is mentioned in the log')
else:
    print('Python is not mentioned in the log')
    
'''

import os

os.rename('./practice/new_name.txt', './practice/new_name1.txt')
    

