# Problem 1
output = []
def flatten_func(input):

    for i in input:
        if type(i) == list or type(i) == set or type(i) == tuple or type(i) == dict:
            flatten_func(i)
        else:
            output.append(i)

    return output

# Problem 2
def reverse_func(input):
    input.reverse()
    for i in input:
        if type(i) == list:
            i.reverse()

    return input
