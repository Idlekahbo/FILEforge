import customtkinter as ctk, json, os, ctypes, sys
from scenes.widgets.controlbuttons import Hamburger
from scenes.widgets.submenus import NavigationMenu
from scenes import DirAudit, DirPDFaTools, FilePDFaTools

if getattr(sys, "frozen", False): basepath = os.path.dirname(sys.executable)
else: basepath = os.path.dirname(os.path.abspath(__file__))
theme = json.load(open(basepath + "\\theme.json", "r"))
settings = json.load(open(basepath + "\\settings.json", "r"))
settings["RuntimeVariables"]["Basepath"] = basepath
window = ctk.CTk(fg_color=theme["Background"])
window.geometry("500x428")
window.title("FILEforge")
window.wm_iconbitmap(basepath + "\\images\\icons\\logo.ico")
window.resizable(False, False)
ctk.set_widget_scaling(settings["WindowScale"])
ctk.set_window_scaling(settings["WindowScale"])
DWMWA_SYSTEMBACKDROP_TYPE = 38
DWMSBT_NONE = 1

ctypes.windll.dwmapi.DwmSetWindowAttribute(
    window.winfo_id(),
    DWMWA_SYSTEMBACKDROP_TYPE,
    ctypes.byref(ctypes.c_int(DWMSBT_NONE)),
    ctypes.sizeof(ctypes.c_int)
)

# content window
content_window = ctk.CTkFrame(master=window, fg_color="transparent", bg_color="transparent", width=500, height=428)
content_window.pack()
DirPDFaTools(content_window, theme, settings)
# submenus | navigation
nm = NavigationMenu(window, theme, settings, content_window, DirAudit, DirPDFaTools, FilePDFaTools)
nm.place(x=nm.x, y=0)
# hamburger | hamburger
hamburger = Hamburger(window, theme, settings, nm.move)
hamburger.place(x=0, y=0)

window.mainloop()