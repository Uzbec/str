import ft_len as lenn


def ft_even_place(str):
    a = ""
    for i in range(lenn.ft_len(str)):
        if i % 2 == 1:
            a += str[i]
    return a
