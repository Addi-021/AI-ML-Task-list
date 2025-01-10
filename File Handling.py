# Script to count the number of words in a text file

def count_words(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            text = file.read()

        # Count the words
        word_count = len(text.split())

        # Write the results to the output file
        with open(output_file, 'w') as file:
            file.write(f"The number of words in the file is: {word_count}\n")

        print(f"Word count written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    input_file = "example_Hello.txt"  # Example input file
    output_file = "example_Hello.txt"  # Example output file

    # Create an example input file for demonstration
    with open(input_file, 'w') as example_file:
        example_file.write("This is a sample text file with some words.")

    # Run the word count function
    count_words(input_file, output_file)

    # Display the output file content
    with open(output_file, 'r') as example_output:
        print(example_output.read())
