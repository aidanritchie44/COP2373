#Using the code in Section 7.4, write a program that will allow me to have any number
# of sentences, including sentences which begin with numbers.
# Display the sentences and the count of sentences.

#import re to prepare code for regular expression
import re

#create main function
def sentence_allower():
    print("Enter your sentences (to finish, type 'done' below last sentence and press enter):")
    input_text = []

#create while loop to allow user to write endless sentences until they choose to end
    while True:
        line = input()
        if line.lower() == 'done':
            break
        input_text.append(line)

#join all lines into a single string
    combined_text = '\n'.join(input_text)

#regular expression to find sentences
    pat = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(.*?[\.\?!])'

#find all sentences with DOTALL and MULTILINE flags
    sentences = re.findall(pat, combined_text, re.DOTALL | re.MULTILINE)

#r.strip to make sure printed sentences come out neat
    sentences = [s.strip() for s in sentences]

#print and display the sentences to user
    print("\nYou entered the following sentences:")
    for s in sentences:
        print(s)

#count and display the number of sentences
    print(f"\nTotal number of sentences: {len(sentences)}")

#call function
if __name__ == "__main__":
    sentence_allower()
