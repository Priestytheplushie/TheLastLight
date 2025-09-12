from rich.console import Console
import sys

def title_screen(console):
    console.print("[purple] Corrupted Shadows [/purple]")
    console.print("[yellow] The Last Light [/yellow]")
    console.print("")
    console.print("1. Play")
    console.print("2. Options")
    console.print("3. Quit")
    while True:
        choice = input("> ")
        if choice == "1":
            return "play"
        elif choice == "2":
            return "options"
        elif choice == "3":
            sys.exit()
        else:
            console.print("[red] Invalid Input! Please enter a valid option [/red]")

def new_game(console):
    console.clear()