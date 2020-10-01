from str import ft_len as lenn


def ft_first_end_three(a):
    if lenn.ft_len(a) > 5:
        return a[0] + a[1] + a[2] + a[-3] + a[-2] + a[-1]
    return a[0] * lenn.ft_len(a)
