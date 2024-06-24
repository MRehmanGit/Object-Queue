class Queue:
    def __init__(self):
        # Initialize the queue with an empty list
        self.__queue_list = []

    def put(self, elem):
        # Add an element to the end of the queue
        self.__queue_list.append(elem)

    def get(self):
        # Remove and return the element from the front of the queue
        final_value = self.__queue_list[0]
        del self.__queue_list[0]
        return final_value

    def length(self):
        # Return the number of elements in the queue
        return len(self.__queue_list)


class SuperQueue(Queue):

    def __init__(self):
        # Initialize the super queue by calling the base class initializer
        Queue.__init__(self)

    def isempty(self):
        # Check if the length of the data structure is 0
        if self.length() == 0:
            return True
        else:
            return False


# Create an instance of SuperQueue
que = SuperQueue()
# Add elements to the queue
que.put(1)
que.put("dog")
que.put("cat")
que.put(False)

# Iterate through the queue and retrieve elements
for i in range(5):
    # Check if the queue is not empty
    if not que.isempty():
        print(que.get())
    else:
        # If empty, print a message indicating the queue is empty
        print("Queue empty")
