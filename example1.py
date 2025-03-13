import tkinter as tk

class TemperatureBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Bar")
        self.value = 20  # Initial temperature
        
        # Setup Canvas
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack(pady=20)
        
        # Draw static elements
        self.canvas.create_rectangle(50, 200, 350, 220, outline="gray")  # Background bar
        self.bar = self.canvas.create_rectangle(50, 200, 50, 220, fill="blue")  # Dynamic bar
        self.canvas.create_text(200, 250, text="°C", font=("Arial", 14))
        
        # Labels
        self.canvas.create_text(50, 180, text="0°C", anchor=tk.W, fill="blue", font=("Arial", 10))
        self.canvas.create_text(200, 180, text="Normal Range: 20-25°C", fill="green", font=("Arial", 10))
        self.canvas.create_text(350, 180, text="30°C", anchor=tk.E, fill="red", font=("Arial", 10))
        
        # Value Entry
        self.entry = tk.Entry(root, width=10)
        self.entry.pack(side=tk.LEFT, padx=10)
        self.btn = tk.Button(root, text="Update", command=self.update_value)
        self.btn.pack(side=tk.LEFT)
        
        self.update_display()
    
    def update_value(self):
        try:
            self.value = float(self.entry.get())
            self.update_display()
        except ValueError:
            pass
    
    def update_display(self):
        bar_width = (self.value / 30) * 300  # Map 0-30°C to 0-300 pixels
        color = "green" if 20 <= self.value <= 25 else "red"
        self.canvas.coords(self.bar, 50, 200, 50 + bar_width, 220)
        self.canvas.itemconfig(self.bar, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureBar(root)
    root.mainloop()