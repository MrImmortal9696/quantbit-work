from collections import defaultdict

def group_anagrams(words: list) -> list:
    anagram_dict = defaultdict(list)  # Dictionary to store grouped anagrams

    for word in words:
        sorted_word = "".join(sorted(word))  # Sort the word alphabetically
        anagram_dict[sorted_word].append(word)  # Group words with the same sorted value

    return list(anagram_dict.values())  # Convert dictionary values to list

# Example 
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

