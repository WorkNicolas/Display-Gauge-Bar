import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Humidity Sensor")

# Canvas
canvas = tk.Canvas(root, width=650, height=650, bg="white")
canvas.pack()

# Circle
class Circle():
    def __init__(self, x0, y0, x1, y1, fill, outline, width):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.fill = fill
        self.outline = outline
        self.width = width

    def createCircle(self, canvas):
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline=self.outline, fill=self.fill, width=self.width)
        
    def createSmallerCircle(self, canvas, percent, fill, outline, width):
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        circle_radius = (self.x1 - self.x0) / 2 * percent
        
        small_circle_x0 = circle_center_x - circle_radius
        small_circle_y0 = circle_center_y - circle_radius
        small_circle_x1 = circle_center_x + circle_radius
        small_circle_y1 = circle_center_y + circle_radius
        
        canvas.create_oval(small_circle_x0, small_circle_y0, small_circle_x1, small_circle_y1, fill=fill, outline=outline, width=width)
            
    def createArc(self, canvas, percent, fill, outline, width, start_angle, extent_angle):
        # Center Position
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        circle_radius = (self.x1 - self.x0) / 2 * percent
        
        small_circle_x0 = circle_center_x - circle_radius
        small_circle_y0 = circle_center_y - circle_radius
        small_circle_x1 = circle_center_x + circle_radius
        small_circle_y1 = circle_center_y + circle_radius
        
        canvas.create_arc(small_circle_x0, small_circle_y0, small_circle_x1, small_circle_y1, 
                          fill=fill, outline=outline, width=width, 
                          start=start_angle, extent=extent_angle, style=tk.PIESLICE)
        
    def createRectangle(self, canvas, percent, fill, outline, width, offset_y_percent, rect_width_percent):
        # Center Position
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        circle_radius = (self.x1 - self.x0) / 2 * percent
        rect_width = circle_radius * rect_width_percent
        
        # Y Offset
        small_rect_x0 = circle_center_x - rect_width
        small_rect_y0 = circle_center_y - circle_radius + (circle_radius * offset_y_percent)
        small_rect_x1 = circle_center_x + rect_width
        small_rect_y1 = circle_center_y + circle_radius + (circle_radius * offset_y_percent)

        canvas.create_rectangle(small_rect_x0, small_rect_y0, small_rect_x1, small_rect_y1, fill=fill, outline=outline, width=width)
    
    def createMultiLabel(self, canvas, percent, offset_y_percent, rect_width_percent, margin, textLeft, textRight, 
                    x_spread=0, y_offset=0, font=("Arial", 16)):
        # Around Rectangle's Position
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        circle_radius = (self.x1 - self.x0) / 2 * percent
        rect_width = circle_radius * rect_width_percent

        # Spreading text1 and text2
        # Positive x_spread increases distance, negative decreases
        rect_x0 = circle_center_x - rect_width - x_spread
        rect_x1 = circle_center_x + rect_width + x_spread
        
        # Y Axis
        rect_y1 = circle_center_y + circle_radius + (circle_radius * offset_y_percent) + y_offset

        # Adjust Positions
        canvas.create_text(rect_x0 - margin, rect_y1 + margin, text=textLeft, font=font)
        canvas.create_text(rect_x1 + margin, rect_y1 + margin, text=textRight, font=font)
        
    def createLabel(self, canvas, text, y_axis=0, font=("Arial", 16)):
        # Center Position
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        
        # Y Axis
        label_x = circle_center_x
        label_y = circle_center_y + y_axis
        
        # Adjust Positions
        canvas.create_text(label_x, label_y, text=text, font=font)
        
    def createInputField(self, canvas, root, y_axis=0, width=10):
        # Calculate the center position
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        
        # Input Field
        entry = tk.Entry(root, width=width)
        
        canvas.create_window(circle_center_x, circle_center_y + y_axis, window=entry)
        
        return entry


# Create main shapes
shell = Circle(50, 50, 600, 600, "gray", "black", 1)
shell.createCircle(canvas)

# Baseplate
shell.createSmallerCircle(canvas, 0.8, "aliceblue", "black", 2)

# Four Arcs complete a circle
shell.createArc(canvas, 0.6, "orange", "black", 1, 0, 90)
shell.createArc(canvas, 0.6, "orange", "black", 1, 90, 90)
shell.createArc(canvas, 0.6, "orange", "black", 1, 180, 90)
shell.createArc(canvas, 0.6, "orange", "black", 1, 270, 90)

# White Circle 
shell.createSmallerCircle(canvas, 0.45, "aliceblue", "black", 1) 

# White Rectangle (label_opening)
shell.createRectangle(canvas, 0.25, "aliceblue", "black", 0, 1.45, 1.2)

# Multi Label
shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "0", "100", x_spread=0, y_offset=0)
shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "10", "90", x_spread=60, y_offset=-50)
shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "20", "80", x_spread=100, y_offset=-120)
shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "30", "70", x_spread=103, y_offset=-200)
shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "40", "60", x_spread=60, y_offset=-290)

# Single Label
shell.createLabel(canvas, "50", -190)
shell.createLabel(canvas, "Humidity %", 110)

# Input Field
humidity_input = shell.createInputField(canvas, root, y_axis=150, width=15)

# Run
root.mainloop()
