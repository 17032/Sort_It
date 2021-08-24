# import everything from tkinter module
from tkinter import *
import random


class Home:
    def __init__(self):

        # Formatting variables...
        background_color = "#FFFFFF"
        font_color = "black"
        paragraph_font = "Arial 15"

        # Main Screen GUI...
        self.home_frame = Frame(bg=background_color, pady=10)
        self.home_frame.grid()

        # Sort Heading (row 0)
        self.heading_label = Label(self.home_frame, text="Sort It",
                                      font="Arial 23 bold", fg=font_color,
                                      padx=30, pady=30)
        self.heading_label.grid(row=0)

        # User instructions (row 1)
        self.instruction_label = Label(self.home_frame,
                                          text="Scan for Plastics", font="OpenSans 19 bold",
                                          bg="#68DDA0", fg="#FFFFFF",
                                          pady=20,)
        self.instruction_label.grid(row=1, pady=5)

        # Information on scanner button (row 2)
        self.delivery_button = Button(self.home_frame,
                                      text="How does the scanner work?", font=paragraph_font,
                                      padx=10,pady=10)
        self.delivery_button.grid(row=2, pady=5)

        # Types of Plastic button (row 3)

        self.pickup_button = Button(self.home_frame, text="The Types of Plastic",
                                    font=paragraph_font,
                                    padx=10, pady=10)
        self.pickup_button.grid(row=3, pady=5)

        # Tips button (row 4)
        self.tips_button = Button(self.home_frame, text="Tips to Reduce Plastic ", 
                                  font=paragraph_font, padx=20, pady=10)
        self.tips_button.grid(row=4, pady=5)

        # Questions button (row 4)
        self.question_button = Button(self.home_frame, text="Frequently Asked Questions", 
                               font=paragraph_font, padx=20, pady=10)
        self.question_button.grid(row=5, pady=5)

        
        # Footer bar (row 6)
        self.footer_label = Label(self.home_frame, text="© Sashika Ragvan 2021",
                                  font=paragraph_font, fg="#FFFFFF",
                                  bg="#68DDA0", padx=125, pady=15)
        self.footer_label.grid(row=6, pady=170)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Sort It")
    root.geometry("400x600")
    something = Home()
    root.mainloop()
