class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.index = 0

    def append(self, item):
        # if there's space in buffer, add the item
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)

        # if there's no space in buffer, replace item at current index
        # and increase index by 1
        else:
            self.buffer[self.index] = item
            self.index += 1

        # if index ever equals capacity, reset index back to 0
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        final = []
        for item in self.buffer:
            final.append(item)

        return final