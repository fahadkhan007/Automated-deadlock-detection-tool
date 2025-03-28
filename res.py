class ResourceManager:
    def __init__(self, total_resources, available_resources):
        self.total_resources = total_resources  # Total system resources
        self.available_resources = available_resources  # Available resources

    def allocate(self, process, request):
        """Allocates requested resources to a process if possible."""
        if all(request[i] <= self.available_resources[i] for i in range(len(request))):
            self.available_resources = [self.available_resources[i] - request[i] for i in range(len(request))]
            process.allocated = [process.allocated[i] + request[i] for i in range(len(request))]
            return True
        return False

    def release(self, process):
        """Releases resources held by a process."""
        self.available_resources = [self.available_resources[i] + process.allocated[i] for i in range(len(process.allocated))]
        process.allocated = [0] * len(process.allocated)
