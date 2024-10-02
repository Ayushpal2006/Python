arr = [1,2,3,4,5,5,4,7,4]
l = len(arr)

hash_map = {}

for i in arr:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
        
        
print(hash_map)

# highest_freq = max(hash_map.values())

# highest_freq_elements = [key for key, value in hash_map.items() if value == highest_freq]

# # Output results
# print(f"Highest Frequency: {highest_freq}")
# print(f"Element(s) with Highest Frequency: {highest_freq_elements}")


max_key = max(hash_map, key=hash_map.get)
max_value = hash_map[max_key]

min_key = min(hash_map, key=hash_map.get)
min_value = hash_map[min_key]

print(f"Element with highest frequency: {max_key} ({max_value})")
print(f"Element with lowest frequency: {min_key} ({min_value})")

