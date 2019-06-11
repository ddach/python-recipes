def measure_seq_len(seq):
    if seq == "":
        return []
    prev_letter = seq[0]
    longest_sequence = [prev_letter]
    current_sequence = [prev_letter]
    for l in seq[1:]:
        #print(l, l > prev_letter)
        if l > prev_letter:
            current_sequence.append(l)
        else:
            current_sequence = []
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
        prev_letter = l
    return longest_sequence

if __name__ == "__main__":
    print(measure_seq_len("abcdaabcghilmbaijklmnoyz"))
    print(measure_seq_len("zxya"))
    print(measure_seq_len(""))

