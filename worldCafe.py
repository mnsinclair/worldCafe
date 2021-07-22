
from itertools import permutations
from random import choices
import numpy as np
import pandas as pd

def order_finder(num_tables, num_rounds, num_guests, max_difference):
    # start table index at 1
    tables = [x+1 for x in range(num_tables)]
    perms = [perm for perm in permutations(tables)]
    
    found = False
    while not found:
        #  select candidate sample of permutations
        candidate = np.array(choices(perms, k=num_guests))
        all_rounds_ok = True
        #  for each 'round' in the permutation...
        for discussion_round in candidate.T:
            
            tables, counts = np.unique(discussion_round, return_counts = True)
            #  ...check that the difference between all table counts is below the threshold...
            if max(counts) - min(counts) > max_difference:
                all_rounds_ok = False
                break
        found = all_rounds_ok
    #  Write the suitable candidate to a .csv file
    candidate = pd.DataFrame(candidate)
    candidate.to_csv('Table_orders.csv')


num_of_tables = int(input('How many tables?'))
num_rounds = int(input('How many rounds?'))
num_guests = int(input('How many guests?'))
max_difference = int(input('How big can the difference between the largest and smallest table be? The smaller this value, the longer the algorithm will take.'))


print('Working...')
order_finder(num_of_tables, num_rounds, num_guests, max_difference)
print('Done.')
print('Please check the folder from which you ran this script (sequences have been written to a spreadsheet)')