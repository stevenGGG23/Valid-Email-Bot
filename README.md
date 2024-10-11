This Python script processes a given file, extracts valid email addresses,
and writes them to an output file named results.out. The program reads the input file specified by the user,
splits its content into individual words, and checks each word for the presence of an email address using the is_valid_email 
function. If a valid email address is found (i.e., contains '@' and a domain with a '.'), it is cleaned of any trailing characters like commas or angle brackets and added to a list of valid emails. Finally, all valid emails are written to the output file. If the specified input file does not exist, an error message is displayed.

