import ft_len as l


def ft_find_str(str1, str2):
    if str2 in str1:
        for i in range(l.ft_len(str1)):
            for j in str2:
                if str1[i] == j:
                    if str1[i:l.ft_len(str2) + i] == str2:
                        return i
    return -1
