def main():
    file_name = input("Enter file to process: ")
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        
        words = data.split()
        valid_emails = []

        for word in words:
            if '@' in word:
                valid_email = is_valid_email(word)
                if valid_email:
                    valid_emails.append(valid_email)

        with open('results.out', 'w') as out_file:
            for email in valid_emails:
                out_file.write(email + '\n')

    except FileNotFoundError:
        print(f"{file_name} does not exist!")

def is_valid_email(email):
    email = email.strip('<>')
    while email.endswith(','):
        email = email[:-1]
    if '@' in email and '.' in email.split('@')[-1]:
        return email
    return None

if __name__ == "__main__":
    main()
