def selection_sort(numbers):
    for i in range(len(numbers)):
        minimum_index = i
        for j in range(i+1,len(numbers)):
            if numbers[j]<numbers[minimum_index]:
                minimum_index = j
        numbers[i],numbers[minimum_index]=numbers[minimum_index],numbers[i]
    return numbers


numbers=[18,6,66,44,9,2,14]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
