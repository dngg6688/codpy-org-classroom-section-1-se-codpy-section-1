import webbrowser

"""
ToolsHW: A clean version of calculation and video playback.
Following PEP 8 guidelines and Clean Code principles.
"""

def play_video():
    """Opens the specified YouTube video in the default browser."""
    rickroll_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("Correct answer! Playing the victory video...")
    webbrowser.open(rickroll_url)

def calculate_and_verify():
    """Asks a math question and verifies the result."""
    try:
        user_input = input("1 times 1 = ? ")
        # Convert input to integer to perform numerical comparison
        answer = int(user_input)

        if answer == 1:
            play_video()
        else:
            print("Wrong! Try again.")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    except (KeyboardInterrupt, EOFError):
        print("\nProgram terminated.")

if __name__ == "__main__":
    calculate_and_verify()
