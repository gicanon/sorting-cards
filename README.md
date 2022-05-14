# Data Sort Using Cards

A python project to solve a card sorting problem.

Suppose you are sorting a set of cards. The right hand holds several cards which are sequentially sorted by numbers arranged from right to left, say for example, five cards with 10, 6, 5, 3, 2 arranged from right to left. Your left hand is picking up the top card from a pile of card deck. Now you insert the card that you have picked from the pile of deck into the right position within the right-hand cards, in a sorted order from right to left.

Exercise:

**Write** the instructions in a step-by-step manner. Note down even a minor step that you have taken to insert the left-hand card into a correct position within the set of right-hand cards so that the right-hand card set remains sorted from right to left.

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

STEP 7: The random card is inserted in the order from right to left. Print the card list.

- PRINT cardList

## Getting Started

### Dependencies

This python project does not have any external libraries. However, starting this program will only require a Python 3 version.

### Installing

The latest version of python can be installed on the website: https://www.python.org/downloads/.

### Executing program

Executing this python project requires only running the file on the python platform. Then, the user needs to rerun the file to repeat the project.

## Authors

Gianluca Cannone - https://github.com/gicanon

## License

Copyright (c) [2022] [Gianluca Cannone]

Permission is hereby granted, free of charge, to any person obtaining a copy of the project without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, and to permit persons to whom the project is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of this project.

THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROJECT OR THE USE OR OTHER DEALINGS IN THE PROJECT.
