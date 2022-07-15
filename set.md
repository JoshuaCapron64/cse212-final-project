Introduction:

A Set, in the context of computer science and general programming, is an Abstract Data Type capable of holding a specific, finite collection of data. Unlike a Queue, in which the data is inputted and outputted by the user in a linear, sequential fashion, a Set simply holds its items without regard for order. It's not typical for the data within a Set to be altered, and usually programs involving Sets are meant to read through them while looking for specific values. If all the data in a Set is numerical, then it will always be printed in numerical order.

Uses, and why Set is a useful Data Structure:

Since Sets are meant to be read through and interpreted, the various operations correlating to them use that function in a variety of ways. For the following example operators, I will use x as my variable, and S to represent my Set. Users can use is_element_of(x, S) to check that Set to see if the x variable is found within. The operator size(S) can be used to see how many items are within the Set, and see what those items are with enumerate(S). The items within a Set can be altered, through such operators as add(S, x) and remove(S, x), whose functions are self explanatory. Of course, these operators will only work if the specified items are not in there already, or are present within the Set, respectively. Python has its own simplified means of using these operators, as will be demonstrated in the examples below. Sets are also particularly useful for hashing and similar functions, since variables converted from an arbitrary size to a fixed size can be stored within a Set.

Big O Notation:

With the use of hashing, O(1)

Example problem:
```python
class set_example:
    print("Set 1:")
    set1 = {5, 3} #an initial Set; this one will showcase adding to it
    print(set1) #notice how it rearranges the numbers to be in order
"""
Output:

Set 1:
{3, 5}
"""
    set1.add(1) #adds a single element to the Set
    print(set1) #prints the Set now with the previous element added
"""
Output:

{1, 3, 5}
"""
    set1.update([2, 4]) #adds multiple elements to the Set
    print(set1) #prints the updated Set
"""
Output:

{1, 2, 3, 4, 5}
"""
    print("\nSet 2:")
    set2 = {1, 2, 3, 4} #this Set will showcase the removal of items
    print(set2)
"""
Output:

Set 2:
{1, 2, 3, 4}
"""
    set2.discard(3) #uses discard() to remove an element
    print(set2)
"""
Output:

{1, 2, 4}
"""
    set2.remove(4) #uses remove() to remove an element
    print(set2)
"""
It should be noted that discard() will do nothing if the specified value is
not found in the Set. But remove() will raise and error if the specified value
is not found. Other than this, both are the same in regard to Set alteration.

Output:

{1, 2}
"""
    print("\nSet 3:")
    set3 = {"A", "B", "C", "D", "E"} #this Set will showcase element retrieval
    print(set3) #notice how the letters are now scrambled
"""
The Output resulting from this will be a random scrambling of the letters in the Set. The following print statements, however, should be consistent with the comments written next to them, regardless of what order the Set prints itself with.
"""
    print(list(set3)[0]) #prints first element in new order

    print(list(set3)[3]) #prints fourth element in new order

    print(list(set3)[-1]) #goes backwards and prints the last element in the new order

```
The following links lead to a practice problem. In this example, you are given a default Set, and must alter it so that the resulting output is a numerical sequence of numbers 1-10. Make sure to re-print the Set every time you alter it.

On Github:
[Set Practice](https://github.com/JoshuaCapron64/cse212-final-project/blob/main/set_tutorial.py)

On VSCode:
[Set Practice](set_tutorial.py)

Back to Welcome:

On Github:
[Welcome](https://github.com/JoshuaCapron64/cse212-final-project/blob/main/welcome.md)

On VSCode:
[Welcome](welcome.md)