import string

def count_word_frequency(text):
    arr = [word.strip(string.punctuation).lower() for word in text.split()]

    word_counts = {}
    for word in arr:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1


    sorted_ans = sorted(word_counts.keys(), key=lambda x: word_counts[x], reverse=True)
    
    for word in sorted_ans:
        print(f"{word}: {word_counts[word]}")
