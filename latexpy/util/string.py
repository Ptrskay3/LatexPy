def diff(reference: str, sample: str, silent: bool = False):
    reference, sample = str(reference), str(sample)
    same = ""
    for same_index, (char1, char2) in enumerate(zip(reference, sample)):
        if char1 == char2:
            same += char1
        else:
            break
    end1, end2 = reference[same_index:], sample[same_index:]
    if end1.find("\n") != -1:
        end1 = end1[: end1.find("\n")]
    if end2.find("\n") != -1:
        end2 = end2[: end2.find("\n")]
    if not silent:
        print(same + "\n^=^\nR>" + end1 + "\nS>" + end2)
    return same, end1, end2
