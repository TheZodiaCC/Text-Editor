import tkinter as tk
from tkinter import filedialog


class Editor:

    def __init__(self, root):
        root.title("Untitled - PyEditor")
        root.geometry("1600x900")

        font = ("Arial", 20)

        self.txtarea = tk.Text(root, font=font)
        self.scrollbar = tk.Scrollbar(root, command=self.txtarea.yview)
        self.txtarea.configure(yscrollcommand=self.scrollbar.set)
        self.txtarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu()

        self.title = None
        self.filename = "Untitled.txt"

    def menu(self):
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        dropdown = tk.Menu(menubar, tearoff=0)
        dropdown.add_command(label="New", command=self.new_file)
        dropdown.add_command(label="Open", command=self.open_file)
        dropdown.add_command(label="Save", command=self.save_file)
        dropdown.add_command(label="Save As", command=self.save_as)
        dropdown.add_separator()
        dropdown.add_command(label="Exit", command=root.destroy)

        menubar.add_cascade(label="Menu", menu=dropdown)

        aboutmenu = tk.Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Program", command=self.aboutus)

        menubar.add_cascade(label="About", menu=aboutmenu)

    def window_title(self):
        root.title("{} - PyEditor".format(self.title))

    def new_file(self):
        self.txtarea.delete(0.0, tk.END)
        self.title = "Untitled"
        Editor.window_title(self)

    def save_file(self):
        if self.filename:
            try:
                content = self.txtarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(content)

            except Exception as e:
                print(e)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                       ("Python Scripts", "*.py*"),
                                                                                       ("Text File", "*.txt*")])
        if self.filename:
            #self.title = os.path.basename(self.filename)
            self.title = self.filename
            Editor.window_title(self)
            self.txtarea.delete(1.0, tk.END)

            with open(self.filename, "r") as file:
                self.txtarea.insert(1.0, file.read())

    def save_as(self):
        try:
            file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                           ("Python Scripts", "*.py*"),
                                                                                           ("Text File", "*.txt*")])
            content = self.txtarea.get(1.0, tk.END)

            with open(file, "w") as f:
                f.write(content)

            #self.title = os.path.basename(file)
            self.title = file
            Editor.window_title(self)
        except Exception as e:
            print(e)

    def aboutus(self):
        about = tk.Tk()

        about.geometry("250x100")
        about.title("About PyEdit")

        tk.Label(about, text="PyEditor v2 ~ 17.05.2019", font="20").pack(fill=tk.BOTH)
        tk.Label(about, text="Created by Zodiac", font="20").pack(fill=tk.BOTH)

        about.mainloop()


if __name__ == "__main__":

    root = tk.Tk()
    ed = Editor(root)
    root.mainloop()



