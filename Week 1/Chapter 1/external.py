import sys
from colorama import Fore, Back, Style, init

# Detect if running inside an IDE (Thonny, IDLE, PyCharm, VSCode) 
# IDE consoles do NOT support ANSI colors — isatty() returns False in IDEs
is_real_terminal = hasattr(sys.stdout, "isatty") and sys.stdout.isatty()

if is_real_terminal:
    # --- RUNNING IN REAL TERMINAL (CMD / PowerShell) ---
    # init() enables Windows ANSI color support
    init(autoreset=True)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print(Fore.GREEN   + "[SUCCESS] Success message in GREEN")
    print(Fore.RED     + "[ERROR]   Error message in RED")
    print(Fore.BLUE    + "[INFO]    Info message in BLUE")
    print(Fore.YELLOW  + "[WARNING] Warning message in YELLOW")
    print(Fore.CYAN    + "[CYAN]    Cyan colored message")
    print(Fore.MAGENTA + "[MAGENTA] Magenta colored message")
    print(Style.BRIGHT + Fore.WHITE  + "[BRIGHT]  Bright WHITE bold text")
    print(Back.RED     + Fore.WHITE  + "  Error background    ")
    print(Back.GREEN   + Fore.BLACK  + "  Success background  ")
    print(Back.YELLOW  + Fore.BLACK  + "  Warning background  ")
    print(Style.RESET_ALL + "Back to normal color")

