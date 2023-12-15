'''
A program to output the sequence length of a fasta file using a for loop
Input: Sequence containing fasta file
Output: the sequence length
Lakshan Jayasinghe
16/11/2022
'''

# variables
count = 0
seq = ''

# Opening fasta file
with open(r"D:\Pycharm workspace\Lab2\sequence (2).fasta") as file:

    for line in file:

# Remove \n characters at the begining and end of the string using strip() function.
        line = line.strip()

# except the empty string lines.

        if line != '\n':
# Add the line to the string ‘seq’ except for header line
            if ">" not in line:
                seq = seq + line


# Print the sequence length
print(len(seq))

# Closing the file
file.close()


