from process import Process
from res import ResourceManager
from bankers_algorithm import BankersAlgorithm
from detection import DeadlockDetector

def main():
    num_processes = int(input("Enter the number of processes: "))
    num_resources = 3  # Fixed to 3 resource types

    print("\nEnter total resources available for each type (3 values expected):")
    total_resources = list(map(int, input().split()))

    print("\nEnter currently available resources for each type (3 values expected):")
    available_resources = list(map(int, input().split()))

    processes = []
    for i in range(num_processes):
        print(f"\nEnter max demand for Process {i} (3 values expected):")
        max_demand = list(map(int, input().split()))

        print(f"Enter allocated resources for Process {i} (3 values expected):")
        allocated = list(map(int, input().split()))

        processes.append(Process(i, max_demand, allocated))

    resource_manager = ResourceManager(total_resources, available_resources)
    bankers_algorithm = BankersAlgorithm(processes, resource_manager)
    deadlock_detector = DeadlockDetector(bankers_algorithm)

    result = deadlock_detector.detect_deadlock()
    print("\n" + result)

if __name__ == "__main__":
    main()
