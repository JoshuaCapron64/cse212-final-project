import queue

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
