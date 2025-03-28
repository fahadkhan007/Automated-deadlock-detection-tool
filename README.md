# 🛠 Automated Deadlock Detection Tool (Banker's Algorithm)

A Python-based **Deadlock Detection Tool** with a **Tkinter GUI** that uses the **Banker’s Algorithm** to analyze process dependencies and resource allocation, identifying potential deadlocks in a system. The tool visually represents resource allocation and safe sequences using **matplotlib** graphs.

## ✨ Features  
✅ User-friendly **GUI** built with Tkinter  
✅ **Graphical Representation** of process-resource allocation  
✅ Uses **Banker’s Algorithm** to detect deadlocks  
✅ Supports **custom input** for processes and resources  
✅ Displays **safe sequences** and alerts if a deadlock occurs  

## 📌 How It Works  
1. **Input Data**: Enter the number of processes, total resources, and available resources.  
2. **Add Processes**: Define the **maximum demand** and **allocated resources** for each process.  
3. **Run Deadlock Detection**: The tool checks for deadlocks and provides a **safe execution sequence** if no deadlock is detected.  
4. **Graph Visualization**: The tool generates a **resource allocation graph** to visually analyze process-resource interactions.  

## 🖥 Setup & Run  
1. Clone the repository:  
   ```sh
   git clone https://github.com/fahadkhan007/Automated-deadlock-detection-tool.git
   cd Automated-deadlock-detection-tool
   ```  
2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```  
3. Run the GUI:  
   ```sh
   python gui.py
   ```  

## 📸 Screenshots  
![graph_proj_png](https://github.com/user-attachments/assets/ef5b2a18-cbf4-40d7-a59d-78e8c5d3c5f3)


## ⚡ Tech Stack  
- **Python**  
- **Tkinter** (GUI)  
- **Matplotlib** (Graph Visualization)  

## 📌 Future Enhancements  
- Add real-time system monitoring for deadlock detection  
- Improve graph interactivity  

🚀 **Contributions are welcome!** If you’d like to improve the tool, feel free to fork and create a pull request.

