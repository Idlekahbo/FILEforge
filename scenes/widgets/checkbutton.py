import customtkinter as ctk, os
from PIL import Image

class BigCheckButton(ctk.CTkButton):
    def __init__(self, master, theme, settings, app, state):
        """
        Parameters:
            master (tkinter widget): parent widget
            theme (dict): theme dictionary
            app (str): name of the application
            state (bool): state of the CheckButton
        """
        self.state = state
        self.states = {}
        # opens image then edits it
        off = Image.open(settings["RuntimeVariables"]["Basepath"] + "\\images\\checkbuttonbig.png")
        off = self.create_img(off, (255, 255, 255), theme["Foreground"])
        off = self.create_img(off, (0, 0, 0), theme[app]["Normal"])
        self.states[True] = ctk.CTkImage(light_image=off, dark_image=off, size=(40, 40)) # assigns
        # edits the off image to be on
        on = self.create_img(off, tuple(int(theme[app]["Normal"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4)), theme["Background"])
        self.states[False] = ctk.CTkImage(light_image=on, dark_image=on, size=(40, 40)) # assigns
        super().__init__(master, image=self.states[self.state], command=self.toggle_state, text="", width=40, height=40, bg_color="transparent", fg_color="transparent", hover=False, corner_radius=0, border_width=0)
    def toggle_state(self):
        """
        Toggles the state of the CheckButton and changes the displayed image to correspond to the new state.
        """
        self.state = not self.state
        super().configure(image=self.states[self.state])
    def create_img(self, img, old_color, new_color):
        """
        Parameters:
            img (PIL.Image.Image): Pillow image to be processed
            old_color (tuple): (r, g, b) color to replace
            new_color (str): hex color string to use as replacement (e.g., '#00ff00' or '00ff00')
        Returns:
            PIL.Image.Image: new image with color replaced
        """
        new_color = tuple(int(new_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        img = img.convert('RGB')
        data = img.getdata()
        new_data = [
            new_color if pixel[:3] == old_color else pixel
            for pixel in data
        ]
        img.putdata(new_data)
        return img
    def get_state(self):
        """
        Returns the state of the CheckButton.
        """
        return self.state
    
class SmallCheckButton(ctk.CTkButton):
    def __init__(self, master, theme, settings, app, state):
        """
        Initializes a SmallCheckButton widget.

        Parameters:
            master (tkinter widget): parent widget
            theme (dict): theme dictionary containing colors
            app (str): name of the app
            state (bool): state of the CheckButton
        """
        self.state = state
        self.states = {}
        # opens image then edits it
        off = Image.open(settings["RuntimeVariables"]["Basepath"] + "\\images\\checkbuttonsmall.png")
        off = self.create_img(off, (255, 255, 255), theme["Foreground"])
        off = self.create_img(off, (0, 0, 0), theme[app]["Normal"])
        self.states[True] = ctk.CTkImage(light_image=off, dark_image=off, size=(26, 26)) # assigns
        # edits the off image to be on
        on = self.create_img(off, tuple(int(theme[app]["Normal"].lstrip('#')[i:i+2], 16) for i in (0, 2, 4)), theme["Background"])
        self.states[False] = ctk.CTkImage(light_image=on, dark_image=on, size=(26, 26)) # assigns
        super().__init__(master, image=self.states[self.state], command=self.toggle_state, text="", width=26, height=26, bg_color="transparent", fg_color="transparent", hover=False, corner_radius=0, border_width=0)
    def toggle_state(self):
        """
        Toggles the state of the CheckButton and changes the displayed image to correspond to the new state.
        """
        self.state = not self.state
        super().configure(image=self.states[self.state])
    def create_img(self, img, old_color, new_color):
        """
        Replaces all pixels of old_color with new_color in the given image.

        Parameters:
            img (PIL.Image.Image): image to be processed
            old_color (tuple): (r, g, b) color to replace
            new_color (str): hex color string to use as replacement (e.g., '#00ff00' or '00ff00')

        Returns:
            PIL.Image.Image: new image with color replaced
        """
        new_color = tuple(int(new_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        img = img.convert('RGB')
        data = img.getdata()
        new_data = [
            new_color if pixel[:3] == old_color else pixel
            for pixel in data
        ]
        img.putdata(new_data)
        return img
    def get_state(self):
        """
        Returns the state of the CheckButton.
        """
        return self.state