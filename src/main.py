from rich.console import Console 
import time
import sys
import time
from core.menus import title_screen


console = Console()

def main():
    console.clear()
    option = title_screen(console)
    if option == "play":
        print("Let the games begin!")

main()