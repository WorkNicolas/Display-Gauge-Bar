from tkinter import Tk, Canvas, Frame, BOTH, W

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Lab 9 A & B')
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(15, 25,     #start x,y
        200, 25)                       #end x,y

        canvas.create_line(300, 35, 300, 200, 
        dash=(4, 2))                   #line style
        
        canvas.create_line(55, 85,     #first point
        155, 85,                       #second point
        105, 180,                      #third point
        55, 85)                        #back to first point

        canvas.create_arc(200, 100,    #top left
        260, 160,                      #bottom right
        start=45, extent=135,          #start angle how far to go
        outline='#77f', fill='#f11', width=2)
        
        canvas.create_oval(200, 150,   #top left
        280, 230,                      #bottom right
        outline='#f11', fill='#1f1', width=2)

        canvas.create_rectangle(
            320, 140,                  #top left
            370, 190,                  #bottom right
        outline='#222', fill='#f76')
        
        canvas.create_text(20, 220, anchor=W, font='Purisa', 
        text='Narendra is the greatest!')
        canvas.pack(fill=BOTH, expand=1)
        
root = Tk()
ex = Example()
root.geometry('400x250+300+300')
root.mainloop()
>>>>>>> b898a4e (New Positioning)
