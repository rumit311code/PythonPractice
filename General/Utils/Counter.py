from collections import Counter
from statistics import mode

def most_frequent(List):
    occurence_count = Counter(List)
    print(f"occurence_count |{occurence_count}|")
    print(f"occurence_count.most_common(1) |{occurence_count.most_common(1)}|")
    print(f"occurence_count.most_common(1)[0] |{occurence_count.most_common(1)[0]}|")
    print(f"occurence_count.most_common(1)[0][0] |{occurence_count.most_common(1)[0][0]}|")
    return occurence_count.most_common(1)[0][0]

print(most_frequent([100, 200, 100, 100, 200, 300, 200]))

def most_common(List):
    return (mode(List))

print(most_common([2, 1, 2, 2, 1, 3, 1]))

