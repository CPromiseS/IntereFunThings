import tkinter as tk

class MemeCraftGui:
    def __init__(self, root_title="MemeCraftGui", root_size=(900, 600)) -> None:
        self.root = tk.Tk()
        self.root.title(root_title)
        self.center_window(root_size[0], root_size[1])
        self.root.iconbitmap(r".\resource\icon\MemeCraftIcon.ico")                  # 设置程序图标

    def center_window(self, width, height):                                         # 窗口居中
        screen_width = self.root.winfo_screenwidth()                                # 屏幕宽
        screen_height = self.root.winfo_screenheight()                              # 屏幕高
        center_x = int((screen_width - width) / 2)
        center_y = int((screen_height - height) / 2)
        self.root.geometry(f"{width}x{height}+{center_x}+{center_y}")

    def run(self):
        self.root.mainloop()

