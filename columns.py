def top_column(matrix):
  best_sum = None
  best_col = None

  for col in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
      total += matrix[row][col]

      if best_sum is None or total > best_sum:
        best_sum = total
        best_col = col

  return best_col


# Test cases
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
assert top_column(matrix_1) == 2

matrix_2 = ((1, 2),
            (3, 4))
assert top_column(matrix_2) == 1

matrix_3 = ((3,),
            (4,),
            (9,))
assert top_column(matrix_3) == 0

matrix_4 = ((-2, -1, -3),)
assert top_column(matrix_4) == 1

print("All tests passed!")
print("Finished early? Discuss time & space complexity")