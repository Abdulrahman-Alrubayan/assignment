# Abdulrahman Alrubayan 440017248 section 171

# As an AI language model, I don't have access to NLP libraries. However, here's an example of how you can generate n-grams using Python for Arabic language:

# python 

import re

def generate_ngrams(text, n): # Remove punctuations and convert to lowercase 
    text = re.sub(r'[^\w\s]', '', text).lower() # Split the text into words
    words = text.split() # Generate n-grams
    ngrams = []
    for i in range(len(words)-n+1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)
    return ngrams

# Example usage

text = "اللغة العربية هي لغة جميلة وغنية بالتعابير"
ngrams = generate_ngrams(text, 5)
print(ngrams)



# This code generates n-gram 5 (n=5) from the given Arabic text. 
