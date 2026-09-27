import customtkinter as ctk, scenes.widgets as w, os, subprocess, json
ctk.set_appearance_mode("dark")

class DirAudit():
    def __init__(self, window, theme, settings):
        app = "DirAudit"
        # maintitle | DirAudit
        w.DualColorTitle(window, "Dir", "Audit", theme, settings, app, width=500, height=65).place(x=0, y=0)
        # title | select path for scanning
        w.SubTitleText(window, 10, 65, "Select path for scanning", theme, settings)
        # directory | get directory
        get_dir = w.GetDir(window, theme, settings, app, "C:\\Users")
        get_dir.place(x=10, y=98)
        # radio | include subdir
        include_subdir = w.BigCheckButton(window, theme, settings, app, True)
        include_subdir.place(x=10, y=157)
        # raditext | include subdir
        w.TextCardinal(window, 58, 162, 130, 40, "Include subdirs", tuple(theme["Font"]["BigNormal"]), "left", theme, settings)
        # radio | only include files with ending
        only_include_files_with_ending = w.BigCheckButton(window, theme, settings, app, False)
        only_include_files_with_ending.place(x=188, y=157)
        # raditext | only include files with ending
        w.TextCardinal(window, 236, 162, 130, 40, "Only include files\nwith the ending:", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # input field | only include files with ending
        only_include_files_with_ending_input = ctk.CTkEntry(window, font=tuple(theme["Font"]["BigNormal"]), placeholder_text_color=theme[app]["InputPlaceholderTextColour"], placeholder_text="e.g .csv, .xlsx", width=137, height=33, fg_color=theme["Foreground"], corner_radius=0, border_width=0, text_color=theme["Font"]["Colour"])
        only_include_files_with_ending_input.place(x=353, y=165)
        # title | save directory
        w.SubTitleText(window, 10, 202, "Select output path for file", theme, settings)
        # directory | save directory
        save_dir = w.SaveDir(window, theme, settings, app, "C:\\Users")
        save_dir.place(x=10, y=230)
        # title | select properties
        w.SubTitleText(window, 10, 280, "Select properties for file(s)", theme, settings)
        # radio | name
        name = w.SmallCheckButton(window, theme, settings, app, True)
        name.place(x=21, y=310)
        # raditext | name
        w.TextCardinal(window, 53, 313, 38, 30, "Name", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # radio | size
        size = w.SmallCheckButton(window, theme, settings, app, True)
        size.place(x=96, y=310)
        # raditext | size
        w.TextCardinal(window, 130, 313, 26, 30, "Size", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # radio | location
        location = w.SmallCheckButton(window, theme, settings, app, True)
        location.place(x=161, y=310)
        # raditext | location
        w.TextCardinal(window, 195, 313, 56, 30, "Location", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # radio | type of file
        type_of_file = w.SmallCheckButton(window, theme, settings, app, True)
        type_of_file.place(x=251, y=310)
        # raditext | type of file
        w.TextCardinal(window, 285, 313, 72, 30, "Type of File", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # radio | time created
        time_created = w.SmallCheckButton(window, theme, settings, app, True)
        time_created.place(x=358, y=310)
        # raditext | time created
        w.TextCardinal(window, 390, 313, 87, 30, "Time Created", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # radio | last accessed
        last_accessed = w.SmallCheckButton(window, theme, settings, app, True)
        last_accessed.place(x=128, y=347)
        # raditext | last accessed
        w.TextCardinal(window, 162, 352, 92, 30, "Last Accessed", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # radio | last modified
        last_modified = w.SmallCheckButton(window, theme, settings, app, True)
        last_modified.place(x=252, y=347)
        # raditext | last modified
        w.TextCardinal(window, 283, 352, 92, 30, "Last Modified", tuple(theme["Font"]["Normal"]), "left", theme, settings)
        # submit
        def submit():
            # DirAuditProcess.exe path
            exe_path = os.path.join(settings["RuntimeVariables"]["Basepath"], "DirAuditProcess", "DirAuditProcess.exe")

            if not os.path.exists(exe_path):
                print(f"DirAuditProcess.exe not found at: {exe_path}")
                return

            # Prepare arguments
            args_list = [
                [r"{}".format(get_dir.get_dirpath()), include_subdir.get_state(), only_include_files_with_ending.get_state(),
                only_include_files_with_ending_input.get()],
                [name.get_state(), size.get_state(), location.get_state(), type_of_file.get_state(),
                time_created.get_state(), last_accessed.get_state(), last_modified.get_state()],
                [r"{}".format(save_dir.get_dirpath())]
            ]

            args_json = json.dumps(args_list)  # safely pass as single string argument

            # Launch DirAuditProcess.exe in a new console
            subprocess.Popen(
                [exe_path, args_json],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        w.Submit(window, 10, 383, 480, 35, theme, settings, app, submit)