
# s = input().strip()
s = 'abcdabee'
hash_map = [0] * 256
for char in s:
    # hash_map[ord(char) - ord('a')] += 1
    hash_map[ord(char) ] += 1

# q = int(input().strip())
q = len(s)

for _ in range(q):
    c = input().strip()
    # print(hash_map[ord(c) - ord('a')])
    print(hash_map[ord(c)])

print(hash_map)