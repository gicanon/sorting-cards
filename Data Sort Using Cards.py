#insert a random card in a list of sorted card
import random 

card_list = [10, 6, 5, 3, 2] # array of sorted card right to left
second_card_list = [] # second array for searching cards > random card

#Step 1: pick a random card between 0 - 15
rand_num = random.randint(0,15) 
print(rand_num)

#Step 2: search numbers which is > rand_num by creating a second_ array (second_card_list)
index = 0
for i in range (0, len(card_list)): 
    if card_list[i] > rand_num:
        second_card_list.append(card_list[i])
        index += 1
print(second_card_list)

#Step 3: last element of second_card_list is adjacent number of rand_num, searching index of adjacent number in card_list
count = 0
while count < len(card_list):  
    if not second_card_list:
        sequence_number = 0
        print(second_card_list)
        break
    elif card_list[count] == second_card_list[-1]:
        sequence_number = count
        break
    else: 
        count += 1
print(sequence_number)

#Step 4: Insert rand_num in array (array_c)
if not second_card_list: 
    card_list.insert(sequence_number, rand_num)
else:
    card_list.insert(sequence_number +1, rand_num)


#Step 5: print the sorted array with the random card
print(card_list) 


