import basic
import os

# Request the file path from the user
text = input('insert path >>> ')

# Ensure the file path isn't empty
if text.strip() == "":
    print("No file path provided!")
else:
    # Check if the file has a .vrll extension
    if not text.endswith(".vrll"):
        print("Error: The file must have a .vrll extension.")
    else:
        try:
            # Open and read the file
            with open(text) as file:
                data = file.read()  # Read the entire content of the file as a string

            # Run the content using the basic.run() function
            result, error = basic.run("<stdin>", data)

            # If there's an error, print it
            if error:
                print(error.as_string())

            # Otherwise, print the result
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))

        except FileNotFoundError:
            print(f"Error: The file at {text} was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")