# Program to return the number of occurrences
# of a pair of characters (pair) in a DNA string (dna).

# To take input from the user
sequence = (input("Enter DNA string to be analysed: "))
pair = (input("Enter character pair to be counted: "))

# Function to find the character pair in the DNA sequence

def count_pairs(sequence,pair):
    count = 0
    while (len(sequence) >0):
       # Get the position of the pair in the sequence
       start = sequence.find(pair)
       if(start >= 0):
           #print (sequence)
           count = count +1
       sequence = sequence[start+2 :]
    return(count)

# Call the function that returns the count value
paircount = count_pairs(sequence, pair)
if paircount > 0:
   print ("The pair occurs %d number of times", paircount)
elif paircount == 0:
   print ("The pair could not be found") 
