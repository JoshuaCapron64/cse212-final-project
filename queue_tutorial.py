"""
Introduction:
A Queue, in the context of computer science and general programming, refers to a linear,
sequential list of entities that allows for more to be added to from the back, and removed
from the front. It is an easy and usually noncomplex way to store a collection of variables,
functions, classes, etc. within one collection inside a code. 

Uses, and why Queue is a useful Data Structure:
Programmers can use the enqueue() function to add new entities into the queue, and the 
dequeue() function to remove entities from the queue. It should be noted that because of 
the natural way that the Queue Data Structure is desinged to work, that everything that 
goes through a queue must be done in a linear sequence. Because of this, enqueue() will
always insert things into the back of the queue, and dequeue() will always remove whatever
is at the front of the queue. This type of linear sequence is usually referred to as
first-in-first-out, or FIFO. This allows for the storing of necessary related entities to
be processed and used for later, essentially acting as a form of a buffer. It also serves
to accomplish breadth-first searches compatible with Trees, as discussed in a different
tutorial. Python has its own simplified means of utilizing the aforementioned operators,
as I will demonstrate in the examples below.

Big O Notation:
As pertaining to Space or Searching: O(n)
As pertaining to Inserting or Deleting: O(1)
"""
import queue

#Example:
class queue_example:
    queue1 = queue.Queue()
    queue2 = queue.Queue()
    def first(queue):
        queue.put('a') #in the basic Queue importation, put() and get() work just like
        queue.put('b') #enqueue() and dequeue() respectively
        queue.put('c')
        print(f"Initial Queue: ")
        for item in queue.queue:
            print(item)
    first(queue1)
    def second(queue):
        queue.get()
        print(f"After removing one item:")
        for item in queue.queue:
            print(item)
    second(queue1)
    def third(queue):
        queue.put('d')
        print(f"After adding one new item: ")
        for item in queue.queue:
            print(item)
    third(queue1)
#Problem:
#You are given a preset queue, and must alter the items so that the resulting
#Queue ends up as "2 4 6 8 10"
class queue_problem:
    #Do not change any of the following code:
    q = queue.Queue()
    def queue_preset(q):
        q.put(64)
        q.put(32)
        q.put(16)
        q.put(10)
        q.put(8)
    queue_preset(q)

    #TODO add whatever code you want here:


    #Do not change any of the following code:
    print("Problem Queue:")
    for item in q.queue:
        print(item)
    