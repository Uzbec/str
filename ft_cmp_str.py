from str import ft_len as l


def ft_cmp_str(str1, str2, num):
    otv = ''
    for i in range(num - 1):
        otv += str1[i]
    otv += str2
    for i in range(num - 1, l.ft_len(str1)):
        otv += str1[i]
    return otv
