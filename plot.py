import matplotlib.pyplot as plt

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

def line(y_values, title='Line plot', xlabel='X axis', ylabel='Y axis'):
    x_values = range(1,len(y_values) + 1)
    plt.plot(x_values, y_values, linewidth=2)
    plt.title(title, fontsize=24)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tick_params(axis='both', labelsize=14)
    plt.show()

def scatter(x_values, y_values, title='Scatter plot', xlabel='X axis', ylabel='Y axis'):
    plt.scatter(x_values, y_values)
    plt.title(title, fontsize=24)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()

if __name__ == "__main__":
    #print(measure_seq_len("abcdaabcghilmbaijklmnoyz"))
    #print(measure_seq_len(""))
    #line([x*x for x in range(1,11)])
    scatter(range(1,1001), [x*x for x in range(1,1001)])

