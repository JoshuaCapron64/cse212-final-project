Introduction:
A Queue, in the context of computer science and general programming, refers to a linear, sequential list of entities that allows for more to be added to from the back, and removed from the front. It is an easy and usually noncomplex way to store a collection of variables, functions, classes, etc. within one collection inside a code.

Uses, and why Queue is a useful Data Structure:
Programmers can use the enqueue() function to add new entities into the queue, and the dequeue() function to remove entities from the queue. It should be noted that because of the natural way that the Queue Data Structure is desinged to work, that everything that goes through a queue must be done in a linear sequence. Because of this, enqueue() will always insert things into the back of the queue, and dequeue() will always remove whatever is at the front of the queue. This type of linear sequence is usually referred to as first-in-first-out, or FIFO. This allows for the storing of necessary related entities to be processed and used for later, essentially acting as a form of a buffer. It also serves to accomplish breadth-first searches compatible with Trees, as discussed in a different tutorial. Python has its own simplified means of utilizing the aforementioned operators, as I will demonstrate in the examples below.

Big O Notation:
As pertaining to Space or Searching: O(n)
As pertaining to Inserting or Deleting: O(1)

Link to example problems:
https://github.com/JoshuaCapron64/cse212-final-project/blob/main/queue_tutorial.py

Back to Welcome:
https://github.com/JoshuaCapron64/cse212-final-project/blob/main/welcome.md