'''
This is a program to ouput the four base counts in a fasta file
Input: sequence containing fasta file
Output: four base counts
Author: Lakshan Jayasinghe
22/11/2022
'''

# declaring four variables to get base counts
A_count = 0
T_count = 0
G_count = 0
C_count = 0

# opening the fasta file in reading mode
with open(r"D:\Pycharm workspace\sequence (2).fasta") as file:
    # reading the entire file
    seq = file.read()
# determining wich base is read and incrementing the base counts
for base in seq:
    if base == "A":
        A_count += 1
    elif base == "T":
        T_count += 1
    elif base == "G":
        G_count += 1
    elif base == "C":
        C_count += 1

print("Adenine count: ", A_count)
print("Thymine count: ", T_count)
print("Guanine count: ", G_count)
print("Cytocine count: ", C_count)

# closing the file
file.close()
