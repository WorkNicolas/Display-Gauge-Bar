import tkinter as tk
import math

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
        left_label_id = canvas.create_text(rect_x0 - margin, rect_y1 + margin, text=textLeft, font=font)
        right_label_id = canvas.create_text(rect_x1 + margin, rect_y1 + margin, text=textRight, font=font)

        # Get coordinates of the created text items
        left_coords = canvas.coords(left_label_id)
        right_coords = canvas.coords(right_label_id)

        return {textLeft: left_coords, textRight: right_coords}

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

    def createLine(self, canvas, target_x, target_y, fill="red", width=5):
        # Calculate the center position
        circle_center_x = (self.x0 + self.x1) / 2
        circle_center_y = (self.y0 + self.y1) / 2
        # Create a line from center to target coordinates with a tag for deletion
        canvas.create_line(circle_center_x, circle_center_y, target_x, target_y,
                        fill=fill, width=width, tags="humidity_line")
        print(f"Line created from ({circle_center_x}, {circle_center_y}) to ({target_x}, {target_y})")


    def onClick(self, canvas, humidity_input):
        try:
            # Convert input to an integer
            humidity = int(humidity_input)
            
            # Validate input is between 0 and 100
            if humidity < 0 or humidity > 100:
                print("Humidity must be between 0 and 100")
                return
            
            # Calculate the center position
            circle_center_x = (self.x0 + self.x1) / 2
            circle_center_y = (self.y0 + self.y1) / 2
            
            # Premade Coordinates based on createMultipleLabels
            coordinates = {
                0: [242.5, 493.4375],
                10: [162.5, 413.4375],
                20: [132.5, 323.4375],
                30: [162.5, 223.4375],
                40: [222.5, 153.4375],
                50: [325, 135],  # Center top position (estimated)
                60: [427.5, 153.4375],
                70: [487.5, 223.4375],
                80: [517.5, 323.4375],
                90: [487.5, 413.4375],
                100: [407.5, 493.4375]
            }
            
            # If exact humidity value exists in coordinates
            if humidity in coordinates:
                target_x, target_y = coordinates[humidity]
            else:
                # Interpolate between the closest known values
                lower_bound = (humidity // 10) * 10
                upper_bound = lower_bound + 10
                
                # Get coordinates for bounds
                lower_x, lower_y = coordinates[lower_bound]
                upper_x, upper_y = coordinates[upper_bound]
                
                # Calculate the fraction between the bounds
                fraction = (humidity - lower_bound) / 10
                
                # Interpolate coordinates
                target_x = lower_x + fraction * (upper_x - lower_x)
                target_y = lower_y + fraction * (upper_y - lower_y)
            
            # Clear previous line as button is clicked
            canvas.delete("humidity_line")
            
            # Create the line from center to target
            self.createLine(canvas, target_x, target_y)
            
        except ValueError:
            print("Please enter a valid number")


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
label_coords = {}
coords_0_100 = shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "0", "100", x_spread=0, y_offset=0)
label_coords.update(coords_0_100)
coords_10_90 = shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "10", "90", x_spread=80, y_offset=-80)
label_coords.update(coords_10_90)
coords_20_80 = shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "20", "80", x_spread=110, y_offset=-170)
label_coords.update(coords_20_80)
coords_30_70 = shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "30", "70", x_spread=80, y_offset=-270)
label_coords.update(coords_30_70)
coords_40_60 = shell.createMultiLabel(canvas, 0.25, 1.45, 1.2, 0, "40", "60", x_spread=20, y_offset=-340)
label_coords.update(coords_40_60)

# Single Label
shell.createLabel(canvas, "50", -190)
shell.createLabel(canvas, "Humidity %", 110)

# Input Field
humidity_input = shell.createInputField(canvas, root, y_axis=150, width=15)

# Button
button = tk.Button(root, text="Submit", command=lambda: shell.onClick(canvas, humidity_input.get()))
canvas.create_window(325, 520, window=button)

# Print the coordinates of each label
print("Coordinates of each label:")
for text, coords in label_coords.items():
    print(f"{text}: {coords}")

# Run
root.mainloop()