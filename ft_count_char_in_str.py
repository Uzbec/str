def ft_count_char_in_str(char, str):
    sc = 0
    for i in str:
        if i == char:
            sc += 1
    return sc
