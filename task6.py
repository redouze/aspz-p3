def recursive_function(counter):
    print(counter, end=" ")
    return recursive_function(counter + 1)

try:
    recursive_function(1)
except RecursionError:
    print("\nСтек перевищено! Ліміт розміру стеку досягнуто.")
