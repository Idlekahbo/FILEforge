import customtkinter as ctk, PIL.Image as Image, os

def ColouriseIcon(img, color):
        """
        Parameters:
            img (PIL.Image.Image): Pillow image to be processed
            old_color (tuple): (r, g, b) color to replace
            color (str): hex color string to use as replacement (e.g., '#00ff00' or '#00ff00')
        Returns:
            PIL.Image.Image: new image with color replaced
        """
        # Convert hex string to RGB tuple
        color = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        # Ensure image has alpha channel
        img = img.convert('RGBA')
        data = img.getdata()
        new_data = []
        for pixel in data:
            r, g, b, a = pixel
            # Replace pixel if it matches old_color (or is very dark)
            if (r, g, b) == (255, 255, 255) or (r < 10 and g < 10 and b < 10):
                new_data.append((color[0], color[1], color[2], a))
            else:
                new_data.append(pixel)
        img.putdata(new_data)
        return img

class FolderIcon(ctk.CTkLabel):
    def __init__(self, master, theme, settings):
        image = ColouriseIcon(Image.open(settings["RuntimeVariables"]["Basepath"] + "\\images\\icons\\folder.png"), theme["Foreground"])
        super().__init__(master, text="", image=ctk.CTkImage(light_image=image, dark_image=image, size=(43, 43)))
class FileIcon(ctk.CTkLabel):
    def __init__(self, master, theme, settings):
        image = ColouriseIcon(Image.open(settings["RuntimeVariables"]["Basepath"] + "\\images\\icons\\file.png"), theme["Foreground"])
        super().__init__(master, text="", image=ctk.CTkImage(light_image=image, dark_image=image, size=(43, 43)))