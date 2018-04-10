# Program to return the number of occurrences
# of a substring on length 'n' (dna_substring) in a DNA string (dna).

# To take input from the user
sequence = (input("Enter DNA string to be analysed: "))
dna_substring = (input("Enter character pair to be counted: "))
length = len(dna_substring)

# Function to find the character pair in the DNA sequence

def count_substring(sequence,dna_substring):
    count = 0
    while (len(sequence) >0):
       # Get the position of the pair in the sequence
       start = sequence.find(dna_substring)
       if(start >= 0):
           #print (sequence)
           count = count +1
       sequence = sequence[start+length:]
    return(count)

# Call the function that returns the count value
substring_count = count_substring(sequence, dna_substring)
if substring_count > 0:
   print ("The substring occurs", substring_count, "times")
elif substring_count == 0:
   print ("The substring could not be found") 
