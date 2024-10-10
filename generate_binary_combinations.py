def generate_binary_combinations(l):
    # Base case: if l is 0, return an empty list
    if l == 0:
        return ['']
    
    # Recursive case: generate combinations of size l-1
    smaller_combinations = generate_binary_combinations(l - 1)
    
    # Add '0' or '1' to each combination of size l-1
    result = []
    for comb in smaller_combinations:
        result.append('0' + comb)
        result.append('1' + comb)
    
    return result
print(generate_binary_combinations(6))