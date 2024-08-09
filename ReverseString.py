def reverse_sentence_with_spaces(sentence):
    # Convert the sentence into a list to handle spaces
    sentence_list = list(sentence)
    
    # Initialize two pointers
    start = 0
    end = len(sentence_list) - 1
    
    # Reverse the characters in the sentence, skipping spaces
    while start < end:
        if sentence_list[start] == ' ':
            start += 1
        elif sentence_list[end] == ' ':
            end -= 1
        else:
            # Swap characters
            sentence_list[start], sentence_list[end] = sentence_list[end], sentence_list[start]
            start += 1
            end -= 1
            
    # Join the list back into a string
    return ''.join(sentence_list)

# Example usage
sentence = "I love Python"
reversed_sentence = reverse_sentence_with_spaces(sentence)
print("Original Sentence: ", sentence)
print("Reversed Sentence: ", reversed_sentence)
