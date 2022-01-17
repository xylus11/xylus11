import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',   
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
]

#Word bank of animals
word_list = ['ant', 'baboon', 'badger' ,
         'wombat', 'zebra ']


#word_list=["ardvark","baboon","camel"]
choice= random.choice(word_list)
lives=6
print(f"{choice} + this is the random word from the choice ")

display=[]
len= len(choice)
for _ in range(len):
    display+="_"
print(display)
end_game= False
while not end_game:
 inp= input("enter the word list :")
 for i in range(len):
    chose =choice[i]
    if chose==inp:
        display[i]=chose
 if inp not in choice:
    lives-=1
    if lives==0:
        end_game=True
        print("you lose")

 print(display)
    
 if "_" not in display:
    end_game=True
    print("you win")
 print(stages[lives])




