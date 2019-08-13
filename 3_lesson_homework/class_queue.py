class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return f'customer {data} added to the queue'
        return f'customer {data} is already in the list'

    def remove_from_queue(self):
        if len(self.queue):
            last_cust = self.queue[-1]
            self.queue.pop()
            return f'last customer in queue {last_cust} removed'
        return 'Queue Empty!'

    def size(self):
        return f'length of queue = {len(self.queue)}'

    def show_all_cust(self):
        return self.queue


# Queue demo

q = Queue()

for i in range(10):
    q.enqueue(f'new_customer_{i}')

print(q.size())
print(q.remove_from_queue())

for customer in q.show_all_cust():
    print(customer)


