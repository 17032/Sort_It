# import everything from tkinter module
from tkinter import *
import random


class Home:
    def __init__(self):

        # Formatting variables...
        background_color = "#FFFFFF"
        font_color = "black"
        paragraph_font = "Arial 13"

        # Main Screen GUI...
        self.home_frame = Frame(width=300, height=300, bg=background_color)
        self.home_frame.grid()

        # Sort Heading (row 0)
        self.ee_heading_label = Label(self.home_frame, text="Sort It",
                                      font="OpenSans 23", fg=font_color,
                                      padx=100, pady=20)
        self.ee_heading_label.grid(row=0)

        # User instructions (row 1)
        self.ee_instruction_label = Label(self.home_frame,
                                          text="Scan for plastics", font=paragraph_font,
                                          wrap=250, bg="#68DDA0",
                                          pady=20)
        self.ee_instruction_label.grid(row=1)

        # Information on scanner button (row 2)
        self.delivery_button = Button(self.home_frame,
                                      text="How does the scanner work?", font=paragraph_font,
                                      fg=font_color, padx=20,
                                      pady=10, compound=LEFT)
        self.delivery_button.grid(row=2)

        # Types of Plastic button (row 3)

        self.pickup_button = Button(self.home_frame, text="Types of Plastic",
                                    font=paragraph_font, fg=font_color,
                                    padx=20, pady=10,
                                    compound=LEFT)
        self.pickup_button.grid(row=3)

        # Tips button (row 4)
        self.tips_button = Button(self.home_frame, text="Tips to Reduce Plastic", 
                                  font=paragraph_font, padx=20, pady=10)
        self.tips_button.grid(row=4)


        # Questions button (row 4)
        self.question_button = Button(self.home_frame, text="Frequently Asked Questions", 
                               font=paragraph_font, padx=20, pady=10)
        self.question_button.grid(row=5)

        
        # Footer bar (row 6)
        self.footer_label = Label(self.home_frame, text="© Sashika Ragvan 2021",
                                  font=paragraph_font, fg=font_color,
                                  bg="#68DDA0", padx=100, pady=20)
        self.footer_label.grid(row=6)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sort It")
    something = Home()
    root.mainloop()
