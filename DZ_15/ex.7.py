from collections import defaultdict
import re

with open('data.txtex7', 'r') as f:
    counts = defaultdict(int)

    for line in f:
        words = re.findall(r'\b\w+\b', line)

        for word in words:
            counts[word] += 1

    for word, counts in sorted(counts.items(), key=lambda x: x[1], reverse=True, )[:5]:
        print(f'{word}: {counts} ')
