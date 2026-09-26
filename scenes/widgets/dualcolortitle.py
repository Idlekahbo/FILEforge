import customtkinter as ctk

def DualColorTitle(parent, text1, text2, theme, settings, app, width=None, height=None):
    frame = ctk.CTkFrame(parent, fg_color="transparent", width=width, height=height)
    if width or height:
        frame.pack_propagate(False)

    inner = ctk.CTkFrame(frame, fg_color="transparent")
    inner.pack(expand=True)

    ctk.CTkLabel(inner, text=text1, text_color=theme["Font"]["Colour"], font=tuple(theme["Font"]["Title"]), fg_color="transparent").pack(side="left")
    ctk.CTkLabel(inner, text=text2, text_color=theme[app]["Title"], font=tuple(theme["Font"]["Title"]), fg_color="transparent").pack(side="left")

    return frame

class DualColorTitleCardinal(ctk.CTkFrame):
    def __init__(self, parent, text1, text2, theme, settings, size, app, side_input, bg, width=None, height=None):

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
        super().__init__(parent, fg_color="transparent", width=width, height=height)
        self.pack_propagate(False)
        ctk.CTkLabel(self, text=text1, text_color=theme["Font"]["Colour"], font=(theme["Font"]["Title"][0], size), fg_color=bg).pack(side=side_input)
        ctk.CTkLabel(self, text=text2, text_color=theme[app]["Title"], font=(theme["Font"]["Title"][0], size), fg_color=bg).pack(side=side_input)
        