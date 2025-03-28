# import tkinter as tk
# from tkinter import ttk, messagebox
# from process import Process
# from res import ResourceManager
# from bankers_algorithm import BankersAlgorithm
# from detection import DeadlockDetector

# class DeadlockGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Deadlock Detection Tool")
#         self.root.geometry("700x600")
#         self.root.configure(bg="#2C3E50") 

        
#         title_label = tk.Label(root, text="Deadlock Detection Tool", font=("Arial", 20, "bold"), bg="#2C3E50", fg="white")
#         title_label.pack(pady=10)

        
#         self.frame_inputs = tk.Frame(root, bg="#34495E", padx=10, pady=10)
#         self.frame_inputs.pack(pady=10, fill="x", padx=20)

#         self.frame_processes = tk.Frame(root, bg="#2C3E50")
#         self.frame_processes.pack(fill="x", padx=20)

#         self.frame_buttons = tk.Frame(root, bg="#2C3E50")
#         self.frame_buttons.pack(pady=10)

       
#         tk.Label(self.frame_inputs, text="Number of Processes:", bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5)
#         self.process_entry = ttk.Entry(self.frame_inputs, width=10)
#         self.process_entry.grid(row=0, column=1, padx=5, pady=5)

        
#         tk.Label(self.frame_inputs, text="Total Resources (3 values):", bg="#34495E", fg="white").grid(row=1, column=0, padx=5, pady=5)
#         self.total_resources_entry = ttk.Entry(self.frame_inputs, width=20)
#         self.total_resources_entry.grid(row=1, column=1, padx=5, pady=5)

        
#         tk.Label(self.frame_inputs, text="Available Resources (3 values):", bg="#34495E", fg="white").grid(row=2, column=0, padx=5, pady=5)
#         self.available_resources_entry = ttk.Entry(self.frame_inputs, width=20)
#         self.available_resources_entry.grid(row=2, column=1, padx=5, pady=5)

        
#         ttk.Button(self.frame_buttons, text="Add Process", command=self.add_process).pack(side="left", padx=10)
#         ttk.Button(self.frame_buttons, text="Run Detection", command=self.run_detection).pack(side="left", padx=10)
#         ttk.Button(self.frame_buttons, text="Clear", command=self.clear_fields).pack(side="left", padx=10)

        
#         self.result_label = tk.Label(root, text="", bg="#2C3E50", fg="yellow", font=("Arial", 12, "bold"))
#         self.result_label.pack(pady=10)

        
#         self.process_data = []

#     def add_process(self):
#         if not self.process_entry.get().isdigit():
#             messagebox.showerror("Error", "Enter a valid number of processes first!")
#             return

#         num_processes = int(self.process_entry.get())

#         if len(self.process_data) >= num_processes:
#             messagebox.showwarning("Warning", "All processes already added!")
#             return

#         frame = tk.Frame(self.frame_processes, bg="#2C3E50", pady=5)
#         frame.pack()

#         tk.Label(frame, text=f"P{len(self.process_data)} Max (3 values):", bg="#2C3E50", fg="white").grid(row=0, column=0, padx=5)
#         max_demand_entry = ttk.Entry(frame, width=20)
#         max_demand_entry.grid(row=0, column=1, padx=5)

#         tk.Label(frame, text=f"P{len(self.process_data)} Allocated (3 values):", bg="#2C3E50", fg="white").grid(row=0, column=2, padx=5)
#         allocated_entry = ttk.Entry(frame, width=20)
#         allocated_entry.grid(row=0, column=3, padx=5)

#         self.process_data.append((max_demand_entry, allocated_entry))

#     def run_detection(self):
#         try:
#             num_processes = int(self.process_entry.get())
#             total_resources = list(map(int, self.total_resources_entry.get().split()))
#             available_resources = list(map(int, self.available_resources_entry.get().split()))

#             if len(total_resources) != 3 or len(available_resources) != 3:
#                 raise ValueError("Must enter exactly 3 values for resources!")

#             processes = []
#             for i, (max_demand_entry, allocated_entry) in enumerate(self.process_data):
#                 max_demand = list(map(int, max_demand_entry.get().split()))
#                 allocated = list(map(int, allocated_entry.get().split()))

#                 if len(max_demand) != 3 or len(allocated) != 3:
#                     raise ValueError("Each process must have exactly 3 values!")

#                 processes.append(Process(i, max_demand, allocated))

#             resource_manager = ResourceManager(total_resources, available_resources)
#             bankers_algorithm = BankersAlgorithm(processes, resource_manager)
#             deadlock_detector = DeadlockDetector(bankers_algorithm)

#             result = deadlock_detector.detect_deadlock()

            
#             messagebox.showinfo("Result", result)
#             self.result_label.config(text=result, fg="lightgreen" if "No Deadlock" in result else "red")

#         except ValueError as e:
#             messagebox.showerror("Input Error", str(e))

#     def clear_fields(self):
#         self.process_entry.delete(0, tk.END)
#         self.total_resources_entry.delete(0, tk.END)
#         self.available_resources_entry.delete(0, tk.END)

#         for frame in self.frame_processes.winfo_children():
#             frame.destroy()
#         self.process_data.clear()

#         self.result_label.config(text="")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DeadlockGUI(root)
#     root.mainloop()





import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from process import Process
from res import ResourceManager
from bankers_algorithm import BankersAlgorithm
from detection import DeadlockDetector

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection Tool")
        self.root.geometry("700x600")
        self.root.configure(bg="#2C3E50") 

        title_label = tk.Label(root, text="Deadlock Detection Tool", font=("Arial", 20, "bold"), bg="#2C3E50", fg="white")
        title_label.pack(pady=10)

        self.frame_inputs = tk.Frame(root, bg="#34495E", padx=10, pady=10)
        self.frame_inputs.pack(pady=10, fill="x", padx=20)

        self.frame_processes = tk.Frame(root, bg="#2C3E50")
        self.frame_processes.pack(fill="x", padx=20)

        self.frame_buttons = tk.Frame(root, bg="#2C3E50")
        self.frame_buttons.pack(pady=10)

        tk.Label(self.frame_inputs, text="Number of Processes:", bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.process_entry = ttk.Entry(self.frame_inputs, width=10)
        self.process_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Total Resources (3 values):", bg="#34495E", fg="white").grid(row=1, column=0, padx=5, pady=5)
        self.total_resources_entry = ttk.Entry(self.frame_inputs, width=20)
        self.total_resources_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Available Resources (3 values):", bg="#34495E", fg="white").grid(row=2, column=0, padx=5, pady=5)
        self.available_resources_entry = ttk.Entry(self.frame_inputs, width=20)
        self.available_resources_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.frame_buttons, text="Add Process", command=self.add_process).pack(side="left", padx=10)
        ttk.Button(self.frame_buttons, text="Run Detection", command=self.run_detection).pack(side="left", padx=10)
        ttk.Button(self.frame_buttons, text="Clear", command=self.clear_fields).pack(side="left", padx=10)

        self.result_label = tk.Label(root, text="", bg="#2C3E50", fg="yellow", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.process_data = []

    def add_process(self):
        if not self.process_entry.get().isdigit():
            messagebox.showerror("Error", "Enter a valid number of processes first!")
            return

        num_processes = int(self.process_entry.get())

        if len(self.process_data) >= num_processes:
            messagebox.showwarning("Warning", "All processes already added!")
            return

        frame = tk.Frame(self.frame_processes, bg="#2C3E50", pady=5)
        frame.pack()

        tk.Label(frame, text=f"P{len(self.process_data)} Max (3 values):", bg="#2C3E50", fg="white").grid(row=0, column=0, padx=5)
        max_demand_entry = ttk.Entry(frame, width=20)
        max_demand_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text=f"P{len(self.process_data)} Allocated (3 values):", bg="#2C3E50", fg="white").grid(row=0, column=2, padx=5)
        allocated_entry = ttk.Entry(frame, width=20)
        allocated_entry.grid(row=0, column=3, padx=5)

        self.process_data.append((max_demand_entry, allocated_entry))

    def run_detection(self):
        try:
            num_processes = int(self.process_entry.get())
            total_resources = list(map(int, self.total_resources_entry.get().split()))
            available_resources = list(map(int, self.available_resources_entry.get().split()))

            if len(total_resources) != 3 or len(available_resources) != 3:
                raise ValueError("Must enter exactly 3 values for resources!")

            processes = []
            for i, (max_demand_entry, allocated_entry) in enumerate(self.process_data):
                max_demand = list(map(int, max_demand_entry.get().split()))
                allocated = list(map(int, allocated_entry.get().split()))

                if len(max_demand) != 3 or len(allocated) != 3:
                    raise ValueError("Each process must have exactly 3 values!")

                processes.append(Process(i, max_demand, allocated))

            resource_manager = ResourceManager(total_resources, available_resources)
            bankers_algorithm = BankersAlgorithm(processes, resource_manager)
            deadlock_detector = DeadlockDetector(bankers_algorithm)

            result = deadlock_detector.detect_deadlock()

            messagebox.showinfo("Result", result)
            self.result_label.config(text=result, fg="lightgreen" if "No Deadlock" in result else "red")

            self.visualize_graph(processes, available_resources)

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def visualize_graph(self, processes, available_resources):
        G = nx.DiGraph()

        for process in processes:
            G.add_node(f"P{process.pid}", color="blue")
            for i in range(3):
                if process.allocated[i] > 0:
                    G.add_edge(f"R{i}", f"P{process.pid}")
                if process.max_demand[i] - process.allocated[i] > 0:
                    G.add_edge(f"P{process.pid}", f"R{i}")

        for i in range(3):
            G.add_node(f"R{i}", color="red")

        plt.figure(figsize=(6, 4))
        colors = [G.nodes[n]['color'] for n in G.nodes]
        nx.draw(G, with_labels=True, node_color=colors, edge_color='gray', font_weight='bold', node_size=2000)
        plt.title("Resource Allocation Graph")
        plt.show()

    def clear_fields(self):
        self.process_entry.delete(0, tk.END)
        self.total_resources_entry.delete(0, tk.END)
        self.available_resources_entry.delete(0, tk.END)

        for frame in self.frame_processes.winfo_children():
            frame.destroy()
        self.process_data.clear()

        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlockGUI(root)
    root.mainloop()
