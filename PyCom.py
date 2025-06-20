from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.padding import Padding
from rich.prompt import Prompt

# It's best to define the console once at the top level
console = Console()

def get_required_input(prompt_text):
    """
    A reusable function that asks the user for input and keeps asking
    until a non-empty value is provided. It shows an error panel if the
    input is empty.
    """
    # Display the initial prompt text, centered
    console.print(Align.center(prompt_text))

    while True:
        # Get input from the user
        user_input = input()

        # Check if the input is valid (not just whitespace)
        if user_input and user_input.strip():
            return user_input.strip()  # Return the valid input
        else:
            # If input is empty, clear the screen and show an error panel
            console.clear()
            error_panel = Panel(
                "This field is required. Please enter a value.",
                title="[bold red]Alert[/bold red]",
                border_style="red"
            )
            padded_error = Padding(error_panel, (3, 0, 0, 0))
            
            # Display the error and then re-display the original prompt below it
            console.print(Align.center(padded_error))
            console.print(Align.center(prompt_text))


def new():
    """
    Gets a new item code and price from the user and writes them to a file.
    """
    console.clear()
    
    # --- Get Item Code ---
    item_code = get_required_input("[green]Please enter the new item code below.[/green]")
    
    # --- Get Item Price ---
    # Clear the screen before asking the next question
    console.clear()
    item_price = get_required_input(f"[green]Please enter the price for item [cyan]{item_code}[/cyan].[/green]")

    # --- Write to File ---
    # Now that we have BOTH values, we can write them to the file.
    try:
        # We use "a" (append mode) so we don't erase the file every time.
        # Use "w" if you want to overwrite the file.
        with open("codes.txt", "a") as f:
            # Format the code and price into a single string line
            f.write(f"{item_code},{item_price}\n")
        
        # Give the user a success message
        console.clear()
        success_message = Panel(
            f"Successfully added:\n"
            f"Code: [yellow]{item_code}[/yellow]\n"
            f"Price: [yellow]{item_price}[/yellow]",
            title="[bold green]Success[/bold green]",
            border_style="green"
        )
        console.print(Align.center(success_message))

    except IOError as e:
        # Handle potential file writing errors
        console.print(f"[bold red]Error:[/bold red] Could not write to file. {e}")

def find_product_price(target_code):
    """
    Searches for a product code in 'products.txt' and returns its code and price.
    """
    try:
        with open('codes.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # 1. Split the line into two parts at the comma
                parts = line.strip().split(',')

                # 2. Check if the line has exactly two parts (code and price)
                if len(parts) == 2:
                    code_from_file = parts[0]
                    price_from_file = parts[1]

                    # 3. Compare the code from the file to the one we're looking for
                    if code_from_file == target_code:
                        # 4. Found it! Convert price to a float and return both.
                        return code_from_file, float(price_from_file)

    except FileNotFoundError:
        print("Error: 'products.txt' not found in the current directory.")
        return None, None
    except ValueError:
        print(f"Error: Invalid price format for code {target_code}.")
        return None, None

    # 5. If the loop finishes, the code was not found.
    return None, None

def save_user_input_to_file(text_from_user):
    with open('cart.txt', 'a', encoding='utf-8') as file:
        file.write(text_from_user + '\n')

def subtotal():
    total_sum = 0.0  # Start with a float to handle decimals
    try:
        with open("cart.txt", 'r', encoding='utf-8') as file:
            # Loop through each line in the file
            for line in file:
                # 1. Strip whitespace and convert the line (string) to a float
                #    We use a nested try-except to gracefully skip any non-numeric lines
                try:
                    number = float(line.strip())
                    # 2. Add the number to our running total
                    total_sum += number
                except ValueError:
                    # This line is not a valid number, so we print a warning and skip it
                    print(f"Warning: Could not convert line to a number. Skipping: '{line.strip()}'")

    except FileNotFoundError:
        return 0.0 # Return 0 if the file doesn't exist

    return total_sum

def clear_cart():
    with open("cart.txt", "w",) as file:
        pass

if __name__ == "__main__":
	new()
