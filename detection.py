from bankers_algorithm import BankersAlgorithm

class DeadlockDetector:
    def __init__(self, bankers_algorithm):
        self.bankers_algorithm = bankers_algorithm

    def detect_deadlock(self):
        """Detects if a deadlock is present."""
        is_safe, safe_sequence = self.bankers_algorithm.is_safe_state()
        if is_safe:
            return f"No Deadlock! Safe sequence: {safe_sequence}"
        return "Deadlock Detected! No safe sequence possible."
