# 3 - Create a script to read a text file, count the number of words, and write the results to a new file.

def count_words_in_file(input_filename, output_filename):
    try:
        # Open the input file and read its contents
        with open(input_filename, 'r') as infile:
            text = infile.read()
        
        # Count the number of words
        words = text.split()
        word_count = len(words)
        
        # Write the result to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(f"Number of words: {word_count}\n")
        
        print(f"Word count written to '{output_filename}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")
count_words_in_file(input_file, output_file)