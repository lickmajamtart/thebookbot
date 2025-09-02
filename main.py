from stats import count_words, count_characters, sort_characters_count
import sys 

# usage if nothing is provided
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


### get_book_text finds the path the file as a path and reads it
def get_book_text(path):
        with open(path) as file:
            return file.read()

        
### main function calls get_the_book fuction to print the coontent    
def main():
    symbols = "=" * 12
    symbols2 = "-" * 11
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_count = sort_characters_count(char_dict)

    
    print(f"{symbols} BOOKBOT {symbols}")
    print(f"Analyzing book found at {path}")
    print(f"{symbols2} Word Count {symbols2}")
    print(f"Found {word_count} total words")
    print(f"{symbols2} Character Count {symbols2}")
    
    for item in sorted_count:
        print(f"{item['char']}: {item['num']}")

    print(f"{symbols} END {symbols}")
        

if __name__ == "__main__":
    main()

