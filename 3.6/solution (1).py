import sys


result = dict()
all_words = []


for line in sys.stdin:
    all_words.extend(line.split())

for item in all_words:
    result[item[-1].upper()] = []

for word in all_words:
    result[word[-1].upper()].append(word.lower())

for key in result:
    print(f"{key} - {', '.join(sorted(set(result[key])))}")

