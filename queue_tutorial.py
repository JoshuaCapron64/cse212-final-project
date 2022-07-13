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
