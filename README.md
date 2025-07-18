# Email Validator

This Python script reads a text file, extracts potential email addresses, validates them using a regular expression, and writes the valid and invalid results to separate output files.

## 📄 Overview

The script performs the following actions:

- Extracts words that resemble email addresses from a text file
- Validates email format using a regular expression
- Outputs valid emails to `results.out`
- Logs invalid emails to `invalid_emails.log`
- Displays a summary of how many valid and invalid emails were found

## ✅ Requirements

- Python 3.x

No third-party libraries are needed. This script uses only built-in Python modules.

## 🚀 How to Use

1. **Prepare your input file**  
   Make sure your text file (e.g., `sample.txt`) contains the content from which you want to extract emails.

2. **Run the script**

   ```bash
   python email_validator.py
