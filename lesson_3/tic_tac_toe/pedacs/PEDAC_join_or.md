#### PEDAC - join_or function
# P
Problem Statement:
Write a function named join_or that produces the following results:
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

Inputs: Takes 3 arguments; a list of numbers, a delimiter and a final joining
word

Outputs: A string with the numbers from the list seperated by the delimiter and
a final joining word before the last number

RULES:
Explicit:
- Takes at least one argument; a list of numbers
- Can take a second argument which is the delimiter between the numbers
- Can take a third argument which is the final joining word at the end
- Must return a string

Implicit: 
- default value for 2nd argument: `,` a comma
- default value for the 3rd argument: `or` (joining word)
- A list with a single element returns just a string with that element
- A list with 2 elements returns a string with the fist element, then joining word, 
then the second element

# E:

# Data Structure:
A list with all the correct elements to be joined into the final string

# Algorithm
1. Define a function that takes 3 arguments: lst, delimiter, final_join
2. Define default values for delimiter=',' and final_join='or'
3. If the length of the list argument is longer than 2:
4. Add the first value to a new list.
5. LOOP For each value from the second till end of lst:
    - If this is the final value, add the joining word, then the final value
    and exit the loop.
    - else: Add the delimiter
    - Add the current number to a new list

6. Add in the 2nd last number, the final_join word, then the last number into the new list.
7. Join the new list together as a string and return it.
8. If the length of the list is shorter than 2, return it as a string

# Alternative A:
1. Get the index and element for each number in lst.
2. LOOP:
3. If index is 0, add element to the list, continue
4. If current index is not the last index, add the delimiter to the list, add the 
current num
5. If it is the final index, add the joiner word, then the final number 
# C