with open("text-1.txt", encoding="utf-8") as f:
    words = f.readlines()

print("Antal ord:", len(words))

lengths = []
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
    lengths.append(len(word.strip()))

longest_word = words[lengths.index(max(lengths))]

print(longest_word)
print("Längd på längsta ordet:", max(lengths))
print(longest)
