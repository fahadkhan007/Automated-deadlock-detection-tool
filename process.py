class Process:
    def __init__(self, pid, max_demand, allocated):
        self.pid = pid
        self.max_demand = max_demand 
        self.allocated = allocated 

    def get_need(self):
        """Returns the remaining resource need of the process."""
        return [self.max_demand[i] - self.allocated[i] for i in range(len(self.max_demand))]
