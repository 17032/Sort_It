# import everything from tkinter module
from tkinter import *
import random


class Home:
    def __init__(self):

        # Formatting variables
        background_color = "#FFFFFF"
        font_color = "black"
        paragraph_font = "Arial 15"

        # Main Screen GUI
        self.home_frame = Frame(bg=background_color, pady=10)
        self.home_frame.grid()

        # Sort Heading (row 0)
        self.heading_label = Label(self.home_frame, text="Sort It",
                                      font="Times 35", fg=font_color,
                                      padx=30, pady=30)
        self.heading_label.grid(row=0)

        # User instructions (row 1)
        photo = PhotoImage(file="scan.png")        
        self.instruction_label = Label(self.home_frame, image=photo)

        self.instruction_label.image = photo
        self.instruction_label.grid(row=1, pady=5)

        # Information on scanner button (row 2)
        photo = PhotoImage(file="how.png")        
        self.scanner_label = Label(self.home_frame,image=photo,
                                      padx=10,pady=10)

        self.scanner_label.image = photo
        self.scanner_label.grid(row=2, pady=5)

        # Types of Plastic button (row 3)
        photo = PhotoImage(file="types.png")        
        self.types_label = Label(self.home_frame,image=photo,
                                      padx=10,pady=10)
        
        self.types_label.image = photo
        self.types_label.grid(row=3, pady=5)

        # Tips button (row 4)
        photo = PhotoImage(file="tips.png")        
        self.tips_label = Label(self.home_frame,image=photo,
                                      padx=10,pady=10)

        self.tips_label.image = photo
        self.tips_label.grid(row=4, pady=5)

        # Questions button (row 5)
        photo = PhotoImage(file="questions.png")        
        self.tips_label = Label(self.home_frame,image=photo,
                                      padx=10,pady=10)

        self.tips_label.image = photo
        self.tips_label.grid(row=5, pady=5)
        
        # Footer bar (row 6)
        self.footer_label = Label(self.home_frame, text="© Sashika Ragvan 2021",
                                  font=paragraph_font, fg="#FFFFFF",
                                  bg="#68DDA0", padx=125, pady=10)
        self.footer_label.grid(row=6, pady=40)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sort It")
    root.geometry("400x600")
    something = Home()
    root.mainloop()
