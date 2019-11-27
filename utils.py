import os, tkinter, tkinter.filedialog, tkinter.messagebox


def get_file_path():
    root = tkinter.Tk()
    root.withdraw()

    fTyp = [("","*.csv")]

    iDir = os.path.abspath(os.path.dirname(__file__))
    file_path = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    if file_path is None:
        exit()
    else:
        return file_path

def get_dir_path():
    root = tkinter.Tk()
    root.withdraw()

    iDir = os.path.abspath(os.path.dirname(__file__))
    dir_path = tkinter.filedialog.askdirectory(initialdir = iDir)
    if dir_path is None:
        exit()
    else:
        return dir_path
