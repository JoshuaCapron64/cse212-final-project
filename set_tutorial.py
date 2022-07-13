#Example:
class set_example:
    print("Set 1:")
    set1 = {5, 3} #an initial Set; this one will showcase adding to it
    print(set1) #notice how it rearranges the numbers to be in order

    set1.add(1) #adds a single element to the Set
    print(set1) #prints the Set now with the previous element added

    set1.update([2, 4]) #adds multiple elements to the Set
    print(set1) #prints the updated Set

    print("\nSet 2:")
    set2 = {1, 2, 3, 4} #this Set will showcase the removal of items
    print(set2)

    set2.discard(3) #uses discard() to remove an element
    print(set2)

    set2.remove(4) #uses remove() to remove an element
    print(set2)
    """
    It should be noted that discard() will do nothing if the specified value is
    not found in the Set. But remove() will raise and error if the specified value
    is not found. Other than this, both are the same in regard to Set alteration.
    """
    print("\nSet 3:")
    set3 = {"A", "B", "C", "D", "E"} #this Set will showcase element retrieval
    print(set3) #notice how the letters are now scrambled

    print(list(set3)[0]) #prints first element in new order

    print(list(set3)[3]) #prints fourth element in new order

    print(list(set3)[-1]) #goes backwards and prints the last element in the new order

#Problem:
#You are given a default Set. You must alter the Set so that the resulting output is a
#numerical sequence of numbers 1-10. Make sure to re-print the Set every time you alter it
class set_problem:
    #Do not change any of the following code:
    your_set = {7, 3, 11, 15, 8, 2}
    print(your_set)

    #TODO add whatever code you want here:


    #Do not change any of the following code:
    print(your_set)
