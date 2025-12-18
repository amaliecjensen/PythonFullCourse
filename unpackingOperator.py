numbers = [1, 2, 3]
print(*numbers)  # vi bruger * til at unpacke
print(1, 2, 3)


values = list(range(5))
values = [*range(5), *"Hello"]
print(values)


# interview question

sentence = "this is a common interview question"


char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
char_freq_sorted = sorted(
    char_freq.items(), key=lambda kv: kv[1], reverse=true)
most_repeated = char_freq_sorted[0]
