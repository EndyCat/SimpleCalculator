from tkinter import *
from tkinter import messagebox as mb

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Comic Sans", 21, "bold"), bg="#54a887", foreground="#000")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 140
        try:
            for bt in btns:
                com = lambda x=bt: self.logicalc(x)
                Button(text=bt, bg="#2f805f", foreground="#000",
                       font=("Comic Sans", 15),
                       command=com).place(x=x, y=y,
                                          width=115,
                                          height=79)
                x += 117
                if x > 400:
                    x = 10
                    y += 81
        except:
            mb.showerror(
                "Ошибка", 
                "Очень много цифр...")
            self.formula = ""
    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#54a887"
    root.geometry("485x550+200+200")
    root.iconbitmap('C:\Python\TKinter\icon.ico')
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()