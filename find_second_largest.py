def find_second_largest(arr):
    # Initialize two variables to store the largest and second largest values
    largest = second_largest = -1
    
    for num in arr:
        # Update largest and second largest accordingly
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    print( second_largest)

find_second_largest([1,2,3,4])
