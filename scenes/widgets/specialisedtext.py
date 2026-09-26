import customtkinter as ctk

class SubTitleText(ctk.CTkFrame):
    def __init__(self, master, x, y, text, theme, settings):
        """
        Parameters:
            master (tkinter widget): parent widget
            x (int): x position of the widget
            y (int): y position of the widget
            width (int): width of the widget
            height (int): height of the widget
            text (str): text to be displayed
            font (str): font style and size
        """
        super().__init__(master, fg_color="transparent", width=480, height=33)
        self.pack_propagate(False)
        ctk.CTkLabel(self, text=text, font=tuple(theme["Font"]["Subtitle"]), fg_color="transparent", text_color=theme["Font"]["Colour"]).pack(expand=True)
        self.place(x=x, y=y)
class TextCardinal(ctk.CTkFrame):
    def __init__(self, master, x, y, width, height, text, font, side_input, theme, settings):

        """
        Parameters:
            master (tkinter widget): parent widget
            x (int): x position of the widget
            y (int): y position of the widget
            width (int): width of the widget
            height (int): height of the widget
            text (str): text to be displayed
            font (str): font style and size
            side_input (str): side to pack the label (e.g. "left", "right", "top", "bottom")
        """
        super().__init__(master, fg_color="transparent", width=width, height=height)
        self.pack_propagate(False)
        ctk.CTkLabel(self, text=text, font=font, text_color=theme["Font"]["Colour"], fg_color="transparent").pack(side=side_input)
        self.place(x=x, y=y)