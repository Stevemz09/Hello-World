

import pickle      # Is the library to create the Persistant

history = {'Archy': (12, 4), 'Betty': (10, 6)}

# Print the rate of success for Betty, (6 out of 10)



# How to add another player to the history dictionary

# history['Claudia'] = (84, 36)



def rate_of_winning(dict, player):
    rate = dict[player][1]/dict[player][0]
    return print('The rate of winnings for', player, 'is',round(rate, 2 ))


file_p = open('historyfile, p','wb')
pickle.dump(history, file_p)
file_p.close()

file_p = open('historyfile, p','rb')
history = pickle.load(file_p)
file_p.close()

# history['Clarissa'] = (100, 95)
#  print(history)

# file_p = open('historyfile, p','wb')
 #pickle.dump(history, file_p)
# file_p.close()


