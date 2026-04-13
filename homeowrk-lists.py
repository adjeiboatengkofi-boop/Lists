def square_sorter(start, end):
    # 1. Create two empty buckets (lists)
    evens = []
    odds = []

    # 2. Go through every number in our range
    for num in range(start, end + 1):
        square = num * num  # Find the square value
        
        # 3. Check if the square is Even or Odd
        if square % 2 == 0:
            evens.append(square) # Put in Even bucket
        else:
            odds.append(square)  # Put in Odd bucket

    # 4. Print the final results
    print("Even Squares:", evens)
    print("Odd Squares:", odds)

# Try it out with numbers from 1 to 10
square_sorter(1, 10)
