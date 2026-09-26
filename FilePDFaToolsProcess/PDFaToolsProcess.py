import json, sys, os, ocrmypdf, signal, msvcrt, time
signal.signal(signal.SIGTERM, lambda: sys.exit(0))
info = json.loads(sys.argv[1])

start = time.perf_counter_ns()
status = "Uncompleted"
print(f"Starting {info[0]}...")

stats = os.stat(info[0])
times = (stats.st_atime, stats.st_mtime)

try:
    ocrmypdf.ocr(info[0], info[0], deskew=info[1], force_ocr=info[2], rotate_pages=info[3], rotate_pages_threshold=1, quiet=True)
    status = "C"
except ocrmypdf.exceptions.PriorOcrFoundError:
    print(f"\033[33m(OCR layer found without force-ocr on) File Skipped\033[0m")
    status = "S"
except Exception as e:
    print(f"\033[31mFile Failed\033[0m")
    status = "F"
ns_time = time.perf_counter_ns() - start
os.utime(info[0], times)
print(f"\nPROCESS COMPLETED IN \033[1m{"{:02}:{:02}:{:02}".format((ns_time//1_000_000_000)//3600, ((ns_time//1_000_000_000)%3600)//60, (ns_time//1_000_000_000)%60)}\033[0m")
if status == "C": print("\033[1;32mFile Completed\033[0m")
elif status == "S": print("\033[33mFile Skipped\033[0m")
elif status == "F": print("\033[1;31mFile Failed\033[0m")
print("\033[0m\033[1mPress any key to exit...")
msvcrt.getch()