from process import Process
from res import ResourceManager

class BankersAlgorithm:
    def __init__(self, processes, resource_manager):
        self.processes = processes  
        self.resource_manager = resource_manager  

    def is_safe_state(self):
        """Checks if the system is in a safe state using the Banker's Algorithm."""
        work = self.resource_manager.available_resources[:]  
        finish = [False] * len(self.processes)  
        safe_sequence = []

        while len(safe_sequence) < len(self.processes):
            allocated = False
            for i, process in enumerate(self.processes):
                if not finish[i] and all(need <= work[j] for j, need in enumerate(process.get_need())):
                    work = [work[j] + process.allocated[j] for j in range(len(work))]
                    finish[i] = True
                    safe_sequence.append(process.pid)
                    allocated = True
                    break  
            
            if not allocated:  
                return False, []

        return True, safe_sequence
