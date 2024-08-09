from collections import Counter

def print_min_repeat_chars(input_string):
    # Create a counter to count the frequency of each character
    char_count = Counter(input_string)
    
    # Find the minimum frequency
    min_count = min(char_count.values())
    
    # Find and print characters with the minimum frequency
    min_chars = [char for char, count in char_count.items() if count == min_count]
    
    print("Characters with the minimum frequency:", min_chars)
    print(f"Minimum frequency: {min_count}")

# Example usage
input_string = "character"
print_min_repeat_chars(input_string)
