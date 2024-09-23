def sort_multiples_of_2_4_6(lst):

    multiples = [x for x in lst if x % 2 == 0 or x % 4 == 0 or x % 6 == 0]
    
    # Sort the identified multiples
    multiples.sort()
    
    sorted_lst = []
    j = 0
    for i in lst:
        if i % 2 == 0 or i % 4 == 0 or i % 6 == 0:
            sorted_lst.append(multiples[j])
            j += 1
        else:
            sorted_lst.append(i)
    
    return sorted_lst

# Input list
input_list = [5, 12, 3, 8, 11, 24, 18, 9, 7, 6]

# Get the sorted list
sorted_list = sort_multiples_of_2_4_6(input_list)

print("Original list:", input_list)
print("Sorted list:", sorted_list)
