import customtkinter as ctk, scenes.widgets as w, os, subprocess, json
ctk.set_appearance_mode("dark")

class DirPDFaTools():
    def __init__(self, window, theme, settings):
        app = "PDFaTools"
        # maintitle | DirAudit
        w.DualColorTitle(window, "PDFa", "Tools", theme, settings, app, width=500, height=65).place(x=0, y=0)
        # title | select directory
        w.SubTitleText(window, 10, 65, "Select directory", theme, settings)
        # directory | get directory
        get_dir = w.GetDir(window, theme, settings, app, "C:\\Users")
        get_dir.place(x=10, y=98)
        # title | select file properties for the file
        w.SubTitleText(window, 10, 148, "Select properties for file(s)", theme, settings)
        # radio | include_subdirs
        include_subdirs = w.SmallCheckButton(window, theme, settings, app, True)
        include_subdirs.place(x=32, y=181)
        # raditext | include_subdirs
        w.TextCardinal(window, 66, 184, 95, 30, "Include Subdirs", ("Roboto Regular", 14), "left", theme, settings)
        # radio | deskew
        deskew = w.SmallCheckButton(window, theme, settings, app, True)
        deskew.place(x=164, y=181)
        # raditext | deskew
        w.TextCardinal(window, 198, 184, 50, 30, "Deskew", ("Roboto Regular", 14), "left", theme, settings)
        # radio | force_ocr
        force_ocr = w.SmallCheckButton(window, theme, settings, app, True)
        force_ocr.place(x=249, y=181)
        # raditext | force_ocr
        w.TextCardinal(window, 283, 184, 64, 30, "Force Ocr", ("Roboto Regular", 14), "left", theme, settings)
        # radio | rotate pages
        rotate_pages = w.SmallCheckButton(window, theme, settings, app, True)
        rotate_pages.place(x=344, y=181)
        # raditext | rotate pages
        w.TextCardinal(window, 378, 184, 87, 30, "Rotate Pages", ("Roboto Regular", 14), "left", theme, settings)
        # icon | folder
        w.FolderIcon(window, theme, settings).place(x=457, y=0)
        # submit
        def submit():
            # DirAuditProcess.exe path
            exe_path = os.path.join(settings["RuntimeVariables"]["Basepath"], "DirPDFaToolsProcess", "DirPDFaToolsProcess.exe")
            # Prepare arguments
            args_list = [get_dir.get_dirpath(), include_subdirs.get_state(), deskew.get_state(), force_ocr.get_state(), rotate_pages.get_state()]
            args_json = json.dumps(args_list)  # safely pass as single string argument
            # Launch DirAuditProcess.exe in a new console
            subprocess.Popen(
                ["cmd", "/k", exe_path, args_json],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        w.Submit(window, 10, 220, 480, 35, theme, settings, app, submit)
