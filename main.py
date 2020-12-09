#===========================
# Imports
#===========================
from os import stat
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import zipfile
import os

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Unzip File Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        fieldset = ttk.LabelFrame(frame, text='Choose Zip File')
        fieldset.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.zipfile_btn = ttk.Button(fieldset, text='Browse Zip', command=self.open_file)
        self.zipfile_btn.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        self.filepath = tk.StringVar()
        self.filepath_entry = ttk.Entry(fieldset, textvariable=self.filepath, width=100, state=tk.DISABLED)
        self.filepath_entry.grid(row=0, column=2, sticky=tk.W, padx=(0, 5), ipady=5)

        self.directory_btn = ttk.Button(fieldset, text='Browse Directory', command=self.choose_directory)
        self.directory_btn.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.directorypath = tk.StringVar()
        self.directory_entry = ttk.Entry(fieldset, textvariable=self.directorypath, width=100, state=tk.DISABLED)
        self.directory_entry.grid(row=1, column=2, sticky=tk.W, padx=(0, 5), ipady=5)

        self.unzip_btn = ttk.Button(fieldset, text='Unzip', command=self.unzip)
        self.unzip_btn.grid(row=2, column=1, columnspan=2, sticky=tk.E, padx=5, pady=(0, 5))

    # ------------------------------------------
    def open_file(self):
        """Open and loads the zip file."""
        self.filepath_entry.config(state=tk.NORMAL)

        try:
            file_types = (('Zip Files', '*.zip'),)
            filename = fd.askopenfilename(title='Open', initialdir='/', filetypes=file_types)
            self.filepath.set(filename)

        except Exception as e:
            return

        self.filepath_entry.config(state=tk.DISABLED)

    def choose_directory(self):
        self.directory_entry.config(state=tk.NORMAL)

        try:
            folder_selected = fd.askdirectory()
            self.directorypath.set(folder_selected)

        except Exception as e:
            return

        self.directory_entry.config(state=tk.DISABLED)

    def unzip(self):
        root = zipfile.ZipFile(self.filepath.get())
        root.extractall(self.directorypath.get())
        root.close()

        os.startfile(f'{self.directorypath.get()}')


#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()