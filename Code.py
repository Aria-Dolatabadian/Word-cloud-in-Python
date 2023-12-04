from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re

# Read the text file
file_path = 'file.txt'  # Replace with the path to your text file
with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Define a list of prepositions, acronyms, and abbreviations to ignore
ignore_words = ['in', 'on', 'at', 'to', 'the', 'and', 'for', 'with', 'of', 'is', 'it', 'etc']

# Remove non-alphabetic characters and convert to lowercase
text_content = re.sub(r'[^a-zA-Z\s]', '', text_content).lower()

# Combine default and custom stopwords
stopwords = set(STOPWORDS) | set(ignore_words)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate(text_content)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
