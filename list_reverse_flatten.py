# Problem 1
new_input = []
def flatten_func(input):

    for i in input:
        if type(i) == list or type(i) == set or type(i) == tuple or type(i) == dict:
            flatten_func(i)
        else:
            new_input.append(i)

    return new_input

# Problem 2
def reverse_func(input):
    input.reverse()
    for i in input:
        if type(i) == list:
            i.reverse()

    return input
