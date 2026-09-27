import customtkinter as ctk, widgets as w, os, subprocess, json
ctk.set_appearance_mode("dark")

class FilePDFaTools():
    def __init__(self, window, theme, settings):
        app = "PDFaTools"
        # maintitle | DirAudit
        w.DualColorTitle(window, "PDFa", "Tools", theme, settings, app, width=500, height=65).place(x=0, y=0)
        # title | select directory
        w.SubTitleText(window, 10, 65, "Select file", theme, settings)
        # directory | get directory
        get_file = w.GetFile(window, theme, settings, app, "C:\\Users")
        get_file.place(x=10, y=98)
        # title | select file properties for the file
        w.SubTitleText(window, 10, 148, "Select properties for file", theme, settings)
        # radio | deskew
        deskew = w.SmallCheckButton(window, theme, settings, app, True)
        deskew.place(x=104, y=181)
        # raditext | deskew
        w.TextCardinal(window, 138, 184, 50, 30, "Deskew", ("Roboto Regular", 14), "left", theme, settings)
        # radio | force_ocr
        force_ocr = w.SmallCheckButton(window, theme, settings, app, True)
        force_ocr.place(x=189, y=181)
        # raditext | force_ocr
        w.TextCardinal(window, 223, 184, 64, 30, "Force Ocr", ("Roboto Regular", 14), "left", theme, settings)
        # radio | rotate pages
        rotate_pages = w.SmallCheckButton(window, theme, settings, app, True)
        rotate_pages.place(x=282, y=181)
        # raditext | rotate pages
        w.TextCardinal(window, 316, 184, 87, 30, "Rotate Pages", ("Roboto Regular", 14), "left", theme, settings)
        # icon | file
        w.FileIcon(window, theme, settings).place(x=457, y=0)
        # submit
        def submit():
            # DirAuditProcess.exe path
            #exe_path = os.path.join(os.path.dirname(__file__), "DirPDFaToolsProcess", "PDFaToolsProcess.exe")
            exe_path = os.path.join(settings["RuntimeVariables"]["Basepath"], "FilePDFaToolsProcess", "FilePDFaToolsProcess.exe")

            if not os.path.exists(exe_path):
                print(f"DirAuditProcess.exe not found at: {exe_path}")
                return

            # Prepare arguments
            args_list = [get_file.get_filepath().replace("\\", "/"), deskew.get_state(), force_ocr.get_state(), rotate_pages.get_state()]
            print(args_list)
            args_json = json.dumps(args_list)  # safely pass as single string argument
            # Launch DirAuditProcess.exe in a new console
            subprocess.Popen(
                [exe_path, args_json],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        w.Submit(window, 10, 220, 480, 35, theme, settings, app, submit)
