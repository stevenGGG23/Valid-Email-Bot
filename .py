import re
import os

# Regular expression for more stringent email validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def main():
    file_name = input("Enter file to process: ")
    
    # Check if the file exists before attempting to open it
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    try:
        # Read the content of the file
        with open(file_name, 'r') as file:
            data = file.read()
        
        words = data.split()
        valid_emails = []
        invalid_emails = []

        # Process each word to extract valid emails
        for word in words:
            # Clean the word of any surrounding punctuation
            word = clean_word(word)
            if word and is_valid_email(word):
                valid_emails.append(word)
            elif word:
                invalid_emails.append(word)

        # Output valid emails to a file
        with open('results.out', 'w') as out_file:
            for email in valid_emails:
                out_file.write(email + '\n')

        print(f"Processing complete. Found {len(valid_emails)} valid emails.")
        
        # Optionally log invalid emails
        if invalid_emails:
            with open('invalid_emails.log', 'w') as log_file:
                for email in invalid_emails:
                    log_file.write(email + '\n')
            print(f"Invalid emails logged in 'invalid_emails.log'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def clean_word(word):
    """Removes surrounding punctuation from a word."""
    word = word.strip('<>,;:()"')  # Strip common punctuation
    return word

def is_valid_email(email):
    """Check if an email is valid using a regex pattern."""
    return re.match(EMAIL_REGEX, email) is not None

if __name__ == "__main__":
    main()
