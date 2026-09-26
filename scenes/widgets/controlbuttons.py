import customtkinter as ctk, os
from PIL import Image
class Submit(ctk.CTkButton):
    def __init__(self, master, x, y, width, height, theme, settings, app, command):
        super().__init__(master, width=width, height=height, text="Submit", text_color=theme["Font"]["Colour"], bg_color=theme[app]["Normal"], hover_color=theme[app]["Title"], fg_color=theme[app]["Normal"], font=tuple(theme['Font']['BigNormal']), command=command)
        self.place(x=x, y=y)
class Hamburger(ctk.CTkButton):
    def __init__(self, master, theme, settings, func):
        # load data and convert to theme colours
        normal_imgdata = Image.open(os.path.join(settings["RuntimeVariables"]["Basepath"], "images", "unselecthamburger.png"))
        normal = self.create_img(normal_imgdata, (0, 0, 0), theme["Foreground"])
        # convert to CTkImage
        normal = ctk.CTkImage(light_image=normal, dark_image=normal, size=(50, 40))

        # load data and convert to theme colours
        hover_imgdata = Image.open(os.path.join(settings["RuntimeVariables"]["Basepath"], "images", "hoverhamburger.png"))
        hover = self.create_img(hover_imgdata, (0, 0, 0), theme["Foreground"])
        # respectfully this next one if for the two colours of the mask image im not just repeating to be thick and stupid mmkay
        hover = self.create_img(hover, (255, 255, 255), theme["NavigationMenu"]["HamburgerHover"])
        # convert to CTkImage
        hover = ctk.CTkImage(light_image=hover, dark_image=hover, size=(50, 40))

        def on_enter(event):
            self.configure(image=hover)
        def on_leave(event):
            self.configure(image=normal)
        def on_press(event):
            self.configure(image=normal)
        def on_release(event):
            self.configure(image=hover)
        super().__init__(master, image=normal, command=func, text="", width=50, height=40, bg_color="transparent", fg_color="transparent", hover=False, corner_radius=0, border_width=0, border_spacing=0, )
        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)
        self.bind("<ButtonPress-1>", on_press)
        self.bind("<ButtonRelease-1>", on_release)
    def create_img(self, img, old_color, new_color):
        """
        Parameters:
            img (PIL.Image.Image): Pillow image to be processed
            old_color (tuple): (r, g, b) color to replace
            new_color (str): hex color string to use as replacement (e.g., '#00ff00' or '00ff00')
        Returns:
            PIL.Image.Image: new image with color replaced
        """
        # Convert hex string to RGB tuple
        new_color = tuple(int(new_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        
        # Ensure image has alpha channel
        img = img.convert('RGBA')
        data = img.getdata()
        
        new_data = []
        for pixel in data:
            r, g, b, a = pixel
            # Replace pixel if it matches old_color (or is very dark)
            if (r, g, b) == old_color or (r < 10 and g < 10 and b < 10):
                new_data.append((new_color[0], new_color[1], new_color[2], a))
            else:
                new_data.append(pixel)
        
        img.putdata(new_data)
        return img
