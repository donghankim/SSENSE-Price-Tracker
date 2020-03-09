from tkinter import *
import tkinter.font as font
from item import Items

class UI():
    def __init__(self):
        self.root = Tk()
        self.root.title("SSENSE Pirce Tracker")
        self.root.geometry("700x600+500+300")
        self.head_font = font.Font(family = "futura", size = 36)
        self.title = Label(self.root, text = "SSENSE Price Tracker")
        self.title['font'] = self.head_font
        
        self.update_widgets()

    def track_click(self):
        url_input = self.url_entry.get()
        self.url_entry.delete(0, 'end')
        Item.set_url(url_input)
        self.update_widgets()

        #continuous check for price udpdate
        self.auto_update()

                
    def update_widgets(self):
        #init widgets
        self.url_label = Label(self.root, text = "Paste URL: ")
        self.url_entry = Entry(self.root, width = 12)
        self.submit_button = Button(self.root, text = "Track!", command = self.track_click)
        self.product_name = Label(self.root, text = Item.name)
        self.product_des = Label(self.root, text = Item.description)
        self.price_frame = LabelFrame(self.root, text = "Price Tracker", padx = 20, pady = 10)
        self.price = Label(self.price_frame, text = Item.price_val)
        self.update_time = Label(self.price_frame, text = " : " + str(Item.date_time))
        self.instr_frame = LabelFrame(self.root, text = "Program Instruction", padx = 10, pady = 10)
        self.instr_text = Text(self.instr_frame, height = 6, width = 70)

        instr_str = "This program allows you to track the price of any item on the popular fashion eCommerce store SSENSE."\
            "Enter the link to the item you want to track. The program automatically refreshes every minuet, and updates the price of"\
            " your item. \n\nMade by Donghan Kim"
        self.instr_text.insert(INSERT, instr_str)
        self.instr_text.config(state = "disabled")

        #grid widgets
        self.title.grid(row = 0, column = 0, columnspan = 4, pady = 15)
        self.url_label.grid(row = 1, column = 0, padx = (45, 10), sticky = "W")
        self.url_entry.grid(row = 1, column = 1, padx = 0, sticky = "E")
        self.submit_button.grid(row = 1, column = 2, sticky = "W")
        self.product_name.grid(row = 2, column = 0, columnspan = 3, padx = (50, 0), pady = (30, 10), sticky = "W")
        self.product_des.grid(row = 3, column = 0, columnspan = 3, padx = (50, 0), sticky = "W")
        self.price_frame.grid(row = 1, column = 3, padx = 80, pady = 20)
        self.price.grid(row = 0, column = 0)
        self.update_time.grid(row = 0, column = 1)
        self.instr_frame.grid(row = 4, column = 0, columnspan = 4, padx = (50, 0), pady = (150, 10), sticky = "W")
        self.instr_text.grid(row = 0, column = 0)
    
    def auto_update(self):
        Item.set_url(Item.url)
        self.update_widgets()
        print("running")
        self.root.after(60000, self.auto_update)

def main():
    App = UI()
    App.root.mainloop()


if __name__ == '__main__':
    # to allow App object access Item object
    Item = Items()
    main()
