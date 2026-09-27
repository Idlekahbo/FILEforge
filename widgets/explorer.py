import customtkinter as ctk


class GetDir(ctk.CTkFrame):
    def __init__(self, master, theme, settings, app, default_path):
        """
        Parameters:
            master (tkinter widget): parent widget
            theme (dict): dictionary containing theme data
            app (dict): dictionary containing app data
            default_path (str): default directory path to be selected
        """
        
        super().__init__(master, width=480, height=50) # puts width and height into the constructor
        
        self.actual_dirpath = default_path
        self.dirpath_stringvar = ctk.StringVar()
        self.dirpath_stringvar.set(self.check_length(self.actual_dirpath))
        dirpath = ctk.CTkEntry(self, width=380, height=50, font=tuple(theme["Font"]["Normal"]), fg_color=theme["Foreground"], text_color=theme["Font"]["Colour"], corner_radius=0, border_width=0, textvariable=self.dirpath_stringvar, state="readonly")
        dirpath.grid(row=0, column=0)

        dirpath_select_button = ctk.CTkButton(self, text="Select Dir", font=tuple(theme["Font"]["Normal"]), text_color=theme["Font"]["Colour"], bg_color=theme[app]["Normal"],hover_color=theme[app]["Title"], fg_color=theme[app]["Normal"], width=100, height=50, corner_radius=0, command=self.get_dir)
        dirpath_select_button.grid(row=0, column=1)
    def check_length(self, string):
        """ 
        If the string is longer than 30 characters, it cuts it from the end and adds 3 dots in front of the remaining string.
        If the string is shorter or equal to 30 characters, it just returns the string.
        """
        if len(string) > 43:
            return F"...{string[len(string) - 43: len(string)]}"
        else:
            return string
    def get_dir(self):
        """
        Opens a file dialog for the user to select a directory. If a directory is chosen, it is stored in self.actual_dirpath and the corresponding stringvar is updated.
        """
        dirpath = ctk.filedialog.askdirectory()
        if dirpath == "": return
        self.actual_dirpath = dirpath
        self.dirpath_stringvar.set(self.check_length(dirpath))

    def get_dirpath(self):
        """
        Returns the currently selected directory path.

        This method retrieves the directory path that was selected by the user
        through the file dialog. If no directory has been selected, it returns
        the default or last known directory path.
        """

        return self.actual_dirpath
class SaveDir(ctk.CTkFrame):
    def __init__(self, master, theme, settings, app, default_path):
        """
        Parameters:
            master (tkinter widget): parent widget
            theme (dict): dictionary containing theme data
            app (dict): dictionary containing app data
            default_path (str): default directory path to be selected
        """
        super().__init__(master, width=480, height=50) # puts width and height into the constructor
        
        self.actual_dirpath = default_path
        self.dirpath_stringvar = ctk.StringVar()
        self.dirpath_stringvar.set(self.check_length(self.actual_dirpath))
        dirpath = ctk.CTkEntry(self, width=380, height=50, font=tuple(theme["Font"]["Normal"]), fg_color=theme["Foreground"], text_color=theme["Font"]["Colour"], corner_radius=0, border_width=0, textvariable=self.dirpath_stringvar, state="readonly")
        dirpath.grid(row=0, column=0)

        dirpath_select_button = ctk.CTkButton(self, text="Select Dir", font=tuple(theme["Font"]["Normal"]), text_color=theme["Font"]["Colour"], bg_color=theme[app]["Normal"],hover_color=theme[app]["Title"], fg_color=theme[app]["Normal"], width=100, height=50, corner_radius=0, command=self.get_dir)
        dirpath_select_button.grid(row=0, column=1)
    def check_length(self, string):
        """ 
        If the string is longer than 30 characters, it cuts it from the end and adds 3 dots in front of the remaining string.
        If the string is shorter or equal to 30 characters, it just returns the string.
        """
        if len(string) > 43:
            return F"...{string[len(string) - 43: len(string)]}"
        else:
            return string
    def get_dir(self):
        """
        Opens a file dialog for the user to select a directory. If a directory is chosen, it is stored in self.actual_dirpath and the corresponding stringvar is updated.
        """
        dirpath = ctk.filedialog.asksaveasfilename(filetypes=[("Excel Files", ".xlsx"), ("Comma Separated Values", ".csv"), ("All Files", "*.*")], defaultextension=".xlsx")
        if dirpath == "": return
        if not dirpath.lower().endswith((".xlsx", ".csv")):
            dirpath += ".xlsx"
        self.actual_dirpath = dirpath
        self.dirpath_stringvar.set(self.check_length(dirpath))

    def get_dirpath(self):
        """
        Returns the currently selected directory path.

        This method retrieves the directory path that was selected by the user
        through the file dialog. If no directory has been selected, it returns
        the default or last known directory path.
        """

        return self.actual_dirpath
class GetFile(ctk.CTkFrame):
    def __init__(self, master, theme, settings, app, default_path):
        """
        Parameters:
            master (tkinter widget): parent widget
            theme (dict): dictionary containing theme data
            app (dict): dictionary containing app data
            default_path (str): default directory path to be selected
        """
        
        super().__init__(master, width=480, height=50) # puts width and height into the constructor
        
        self.actual_filepath = default_path
        self.filepath_stringvar = ctk.StringVar()
        self.filepath_stringvar.set(self.check_length(self.actual_filepath))
        filepath = ctk.CTkEntry(self, width=380, height=50, font=tuple(theme["Font"]["Normal"]), fg_color=theme["Foreground"], text_color=theme["Font"]["Colour"], corner_radius=0, border_width=0, textvariable=self.filepath_stringvar, state="readonly")
        filepath.grid(row=0, column=0)

        filepath_select_button = ctk.CTkButton(self, text="Select File", font=tuple(theme["Font"]["Normal"]), text_color=theme["Font"]["Colour"], bg_color=theme[app]["Normal"],hover_color=theme[app]["Title"], fg_color=theme[app]["Normal"], width=100, height=50, corner_radius=0, command=self.get_file)
        filepath_select_button.grid(row=0, column=1)
    def check_length(self, string):
        """ 
        If the string is longer than 30 characters, it cuts it from the end and adds 3 dots in front of the remaining string.
        If the string is shorter or equal to 30 characters, it just returns the string.
        """
        if len(string) > 43:
            return F"...{string[len(string) - 43: len(string)]}"
        else:
            return string
    def get_file(self):
        """
        Opens a file dialog for the user to select a directory. If a directory is chosen, it is stored in self.actual_dirpath and the corresponding stringvar is updated.
        """
        filepath = ctk.filedialog.askopenfilename(filetypes=[("PDF Files", ".pdf"), ("All Files", "*.*")], defaultextension=".pdf")
        if filepath == "" or not filepath.lower().endswith(".pdf"):
            return
        self.actual_filepath = filepath
        self.filepath_stringvar.set(self.check_length(filepath))

    def get_filepath(self):
        """
        Returns the currently selected directory path.

        This method retrieves the directory path that was selected by the user
        through the file dialog. If no directory has been selected, it returns
        the default or last known directory path.
        """

        return self.actual_filepath