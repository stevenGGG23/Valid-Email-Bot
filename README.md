This Python script processes a given text file to extract and validate email addresses. The script reads the file, identifies words that resemble email addresses, checks their validity using a regular expression, and outputs the valid ones into a results file. Invalid email addresses are also logged into a separate file for auditing purposes.

Features:
Extracts email addresses from a text file.
Validates email format using a regular expression.
Outputs valid emails to a results.out file.
Logs invalid emails to an invalid_emails.log file.
Provides user-friendly feedback on the number of valid emails processed.
Requirements:
Python 3.x
Usage:
Prepare the input file: Ensure that your text file contains the email addresses you want to process.

Run the script:

bash
Copy
Edit
python email_validator.py
Input file: When prompted, enter the path to the file you want to process.

Output:

The valid email addresses will be written to results.out.
Any invalid email addresses will be logged to invalid_emails.log.
Example:
Sample Input (sample.txt):
sql
Copy
Edit
Hello, my email is john.doe@example.com. Please contact me at jane_smith123@company.org.
Here are some invalid emails: johndoe@com, invalidemail@domain..com, test@domain@com.
Sample Output:
results.out:

graphql
Copy
Edit
john.doe@example.com
jane_smith123@company.org
invalid_emails.log:

graphql
Copy
Edit
johndoe@com
invalidemail@domain..com
test@domain@com
Console Output:

pgsql
Copy
Edit
Enter file to process: sample.txt
Processing complete. Found 2 valid emails.
Invalid emails logged in 'invalid_emails.log'.
