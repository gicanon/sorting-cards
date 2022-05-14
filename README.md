# Data Sort Using Cards

Suppose you are sorting a set of cards. The right hand holds several cards which are sequentially sorted by numbers arranged from right to left, say for example, five cards with 10, 6, 5, 3, 2 arranged from right to left. Your left hand is picking up the top card from a pile of card deck. Now you insert the card that you have picked from the pile of deck into the right position within the right-hand cards, in a sorted order from right to left.

## Description

The following pseudocode explain the solution of this problem:

Step 1: Pick with the left hand a random card.

- Import the module random
- GET randomNumber from range 0 - 15

Step 2: The right-hand holds several cards, sorted sequentially from right to left. In this example, the right-hand holds 5 cards arranged from right to left.

- cardList = [10, 6, 5, 3, 2]

Step 3: Create a second empty list.

- secondList = empty list

Step 4: Create a for loop to append all the cards greater than the random card. The last card of the second list is the adjacent card number of the random card, and the last greater number.

- FOR each card of cardList
    - IF one of the cards is greater than randomNumber, THEN
        - APPEND the card in secondList
        - INCREMENT to next card
    - ENDIF
- PRINT secondList

Step 5: Search the sequence number of the left card to insert it into the card list without interrupting the card sequence and create a while loop.

- SET count to 0
- WHILE count is smaller than length of cardList
    - IF secondList is empty, THEN
        - sequenceNumber = 0
        - PRINT Second list
        - BREAK
    - ELSE IF count card entry of cardList is equal to last card of secondList
        - sequenceNumber = count
        - BREAK
    - ELSE
        - INCREMENT count
- PRINT sequenceNumber

Step 6: Insert the random card into the card list without interrupting the card order using the sequence number.

- IF secondList is empty, THEN
    - INSERT randomNumber into the first entry of cardList
- ELSE
    - INSERT randomNumber into sequendNumber + 1 entry of cardList

STEP 7: The left card is inserted in the order from right to left. Print the card list.

- PRINT cardList
