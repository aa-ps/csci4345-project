import ray
from collections import Counter
import re
import os

ray.init()

@ray.remote
def clean_word(word):
    return re.sub(r'\W+', '', word).lower()

@ray.remote
def word_count(document):
    words = document.split()
    cleaned_words = [clean_word.remote(word) for word in words]
    cleaned_words = ray.get(cleaned_words)
    count = Counter(cleaned_words)
    return count

books_dir = 'books'

book_files = [os.path.join(books_dir, filename) for filename in os.listdir(books_dir) if filename.endswith('.txt')]

documents = []

for book_file in book_files:
    with open(book_file, 'r', encoding='utf-8') as file:
        documents.append(file.read())

futures = [word_count.remote(doc) for doc in documents]

results = ray.get(futures)

combined_counts = Counter()
for count in results:
    combined_counts.update(count)

print(combined_counts)

ray.shutdown()
