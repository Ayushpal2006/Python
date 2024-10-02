arr = [1, 2, 3, 4, 5, 5, 4, 7, 4]
l = len(arr)

hash_map = {}

# Count frequencies of each element
for i in arr:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

print("Frequency Map:", hash_map)

# Initialize variables to find highest and lowest frequency elements
highest_freq_element = None
highest_freq = -1
lowest_freq_element = None
lowest_freq = float('inf')

# Iterate through the hash_map to find highest and lowest frequency elements
for key, value in hash_map.items():
    if value > highest_freq:
        highest_freq = value
        highest_freq_element = key
    
    if value < lowest_freq:
        lowest_freq = value
        lowest_freq_element = key

print(f"Highest Frequency Element: {highest_freq_element} (Frequency: {highest_freq})")
print(f"Lowest Frequency Element: {lowest_freq_element} (Frequency: {lowest_freq})")