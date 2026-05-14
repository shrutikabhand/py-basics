# This program reads text from a file and analyzes word frequency.
# It counts how many times each word appears in the file
# and displays the words in descending order of frequency.
# The program uses dictionaries, sorting, file handling,
# and exception handling for efficient text analysis.



try:
    with open("story.txt", "r") as file:
        text = file.read().lower()

    words = text.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Sort by frequency (descending)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("\nWord Frequency:\n")
    for word, count in sorted_freq:
        print(word, ":", count)
    print("--------------------------------------------------------------\n")

except FileNotFoundError:
    print("Error: story.txt not found")
    print("--------------------------END--------------------------------------\n")