class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return f'customer {data} added to the queue'
        return f'customer {data} is already in the list'

    def remove_queue(self):
        if len(self.queue):
            last_cust = self.queue[-1]
            self.queue.pop()
            return f'last customer {last_cust} removed'
        return 'Queue Empty!'

    def size(self):
        return f'length of queue = {len(self.queue)}'


q = Queue()
print(q.enqueue('1_customer'))
print(q.enqueue('2_customer'))
print(q.enqueue('3_customer'))
print(q.remove_queue())
print(q.size())
