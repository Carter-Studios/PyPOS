import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt  # Import Prompt for better input handling

# Assuming you have another file named PyCom.py with the `new` function
from PyCom import new 

# --- Setup ---
console = Console()

def main():
    """The main function to run the application loop."""
    
    # The main application loop. It will run forever until we 'break'.
    while True:
        # --- Display the Main Screen ---
        console.clear()
        
        welcome_panel = Panel(
            "Welcome to PyPOS\n"
            "Enter 'new' to add an item.\n"
            "Enter 'exit' to quit.",
            title="[bold cyan]Main Menu[/bold cyan]",
            border_style="green"
        )
        
        console.print(Align.center(welcome_panel))

        # --- Get User Command ---
        # Use Prompt.ask for a clean, rich-integrated input experience
        command = Prompt.ask("\nEnter command").lower().strip()

        # --- Process the Command ---
        if command == "new":
            # Call the `new` function from your other module
            new()
            # Pause so the user can see the result from the 'new' function
            console.input("\nPress Enter to return to the main menu...")

        elif command == "exit":
            console.print("\n[bold yellow]Shutting down. Goodbye![/bold yellow]")
            break  # This exits the 'while True' loop

        else:
            # Handle unknown commands
            console.print(f"\n[bold red]Error:[/bold red] Unknown command '[yellow]{command}[/yellow]'.")
            time.sleep(2) # Pause for 2 seconds so the user can read the error


if __name__ == "__main__":
    main()

