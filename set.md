Introduction:
A Set, in the context of computer science and general programming, is an Abstract Data Type capable of holding a specific, finite collection of data. Unlike a Queue, in which the data is inputted and outputted by the user in a linear, sequential fashion, a Set simply holds its items without regard for order. It's not typical for the data within a Set to be altered, and usually programs involving Sets are meant to read through them while looking for specific values. If all the data in a Set is numerical, then it will always be printed in numerical order.

Uses, and why Set is a useful Data Structure:
Since Sets are meant to be read through and interpreted, the various operations correlating to them use that function in a variety of ways. For the following example operators, I will use x as my variable, and S to represent my Set. Users can use is_element_of(x, S) to check that Set to see if the x variable is found within. The operator size(S) can be used to see how many items are within the Set, and see what those items are with enumerate(S). The items within a Set can be altered, through such operators as add(S, x) and remove(S, x), whose functions are self explanatory. Of course, these operators will only work if the specified items are not in there already, or are present within the Set, respectively. Python has its own simplified means of using these operators, as will be demonstrated in the examples below.

Big O Notation:
O(log n)

Link to example problems:
https://github.com/JoshuaCapron64/cse212-final-project/blob/main/set_tutorial.py