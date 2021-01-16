def insertion_sort(numbers):
    for i in range(1,len(numbers)):
        key = numbers[i]
        print("key:",key)
        j = i-1
        print("outer j:",j)
        while j>=0 and numbers[j]>key:
            print("number of j:",numbers[j])
            numbers[j+1] = numbers[j]
            j = j-1
            numbers[j+1] = key
        print("inner j:",j)
        print("numbers:",numbers)
    return numbers


numbers =[34,32,4,56,8,0,23,44]
print("numbers(1):",numbers[1])
print("numbers(2):",numbers[2])
sorted_list = insertion_sort(numbers)
print(sorted_list)
