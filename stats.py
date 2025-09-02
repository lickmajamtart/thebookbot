### script to count words in book
def count_words(text):
    words = text.split()
    return len(words)

### script for character count
def count_characters(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char not in char_count:
            char_count[lowercase_char] = 1
        else:
            char_count[lowercase_char] += 1
    
    return char_count

### sorting function
def sort_characters_count(text):
    filtered = {k: v for k, v in text.items() if k.isalpha()}
    output = dict(sorted(filtered.items(), key=lambda item: item[1], reverse=True))
    result = [{"char": k, "num": v} for k, v in output.items()]
    return result   