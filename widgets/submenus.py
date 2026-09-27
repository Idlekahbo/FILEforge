import customtkinter as ctk, widgets as w, os
from PIL import Image

class DualColorTitleCardinall(ctk.CTkFrame):

    def __init__(self, parent, text1, text2, theme, settings, size, app, bg,
                 width=None, height=None):

        super().__init__(
            parent,
            width=width,
            height=height,
            fg_color=bg
        )

        font = (theme["Font"]["Title"][0], size)

        self.title1 = ctk.CTkLabel(
            self,
            text=text1,
            text_color=theme["Font"]["Colour"],
            font=font
        )
        self.title1.pack(side="left")

        self.title2 = ctk.CTkLabel(
            self,
            text=text2,
            text_color=theme[app]["Title"],
            font=font
        )
        self.title2.pack(side="left")

class NavigationMenu(ctk.CTkFrame):
    def __init__(self, master, theme, settings, content_window, DirAudit, DirPDFaTools, FilePDFaTools):
        self.moving = False
        self._move_job = None
        self.step = 4
        self.max_width = 162
        self.x = -162
        self.open = False

        super().__init__(master, fg_color=theme["NavigationMenu"]["Colour"], width=self.max_width, height=428, corner_radius=0)

        self.place(x=self.x, y=0)

        def CreateButton(master, relimgpath, theme, app, height, func):
            base_image = Image.open(settings["RuntimeVariables"]["Basepath"] + relimgpath)
            base_image = base_image.resize((149, height), Image.Resampling.NEAREST)
            base_image = create_img(base_image, (255, 255, 255), theme["Font"]["Colour"])
            base_image = create_img(base_image, (127, 127, 127), theme[app]["Title"])
            normal_image = create_img(base_image, (0, 0, 0), theme["Foreground"])
            hover_image = create_img(base_image, (0, 0, 0), theme["Background"])
            normal = ctk.CTkImage(light_image=normal_image, dark_image=normal_image, size=(149, height))
            hover = ctk.CTkImage(light_image=hover_image, dark_image=hover_image, size=(149, height))

            def on_enter(event):
                sidemenubutton.configure(image=hover)
            def on_leave(event):
                sidemenubutton.configure(image=normal)
            def on_press(event):
                sidemenubutton.configure(image=normal)
            def on_release(event):
                sidemenubutton.configure(image=hover)
            sidemenubutton = ctk.CTkButton(master, image=normal, command=func, text="", width=149, height=height, bg_color="transparent", fg_color="transparent", hover=False, corner_radius=0, border_width=0, border_spacing=0, )
            sidemenubutton.bind("<Enter>", on_enter)
            sidemenubutton.bind("<Leave>", on_leave)
            sidemenubutton.bind("<ButtonPress-1>", on_press)
            sidemenubutton.bind("<ButtonRelease-1>", on_release)
            return sidemenubutton
        def create_img(img, old_color, new_color):
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
        def Reset():
            for widget in content_window.winfo_children():
                widget.destroy()

        def ResetDirAudit():
            Reset()
            DirAudit(content_window, theme, settings)

        def ResetDirPDFaTools():
            Reset()
            DirPDFaTools(content_window, theme, settings)

        def ResetFilePDFaTools():
            Reset()
            FilePDFaTools(content_window, theme, settings)

        CreateButton(self, "\\images\\appbuttons\\DirAudit.png", theme, "DirAudit", 29, ResetDirAudit).place(x=4, y=50)
        CreateButton(self, "\\images\\appbuttons\\DirPDFaTools.png", theme, "PDFaTools", 43, ResetDirPDFaTools).place(x=4, y=83)
        CreateButton(self, "\\images\\appbuttons\\FilePDFaTools.png", theme, "PDFaTools", 43, ResetFilePDFaTools).place(x=4, y=130)
        # ctk.CTkButton(self, width=149, height=29, text="", bg_color=theme["Foreground"], hover_color=theme["NavigationMenu"]["HamburgerHover"], fg_color=theme["Foreground"], command=ResetDirAudit).place(x=8, y=50)
        # DualColorTitleCardinall(self, "Dir", "Audit", theme, 30, "DirAudit", bg=theme["Foreground"], width=149, height=29).place(x=8, y=50)
        # DualColorTitleCardinall(self, "PDFa", "Tools", theme, 27, "PDFaTools", bg=theme["Foreground"], width=149, height=29, command=ResetDirPDFaTools).place(x=8, y=83)
        # DualColorTitleCardinall(self, "PDFa", "Tools", theme, 27, "PDFaTools", bg=theme["Foreground"], width=149, height=29, command=ResetFilePDFaTools).place(x=8, y=116)

    # I GOT REALLY STUMPED OKAY THE STUFF BELOW IS CHATGPT IM SORRY ILL GO BAKC ONCE I KNOW HOW TO FIX
    def move(self):
        self.stop_moving()

        self.moving = True
        target = 0 if not self.open else -self.max_width
        self.open = not self.open

        self._animate(target)

    def _animate(self, target):
        if not self.moving:
            return

        if self.x < target:
            self.x = min(self.x + self.step, target)
        elif self.x > target:
            self.x = max(self.x - self.step, target)
        else:
            self.moving = False
            self._move_job = None
            return

        self.place(x=self.x, y=0)

        self._move_job = self.after(
            10,
            lambda: self._animate(target)
        )

    def stop_moving(self):
        self.moving = False

        if self._move_job:
            self.after_cancel(self._move_job)
            self._move_job = None