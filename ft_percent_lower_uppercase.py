bb = 'QWERTYUIOPASDFGHJKLZXCVBNMЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
mb = 'qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю'


def ft_percent_lower_uppercase(str):
    cbb = 0
    cmb = 0
    for i in str:
        if i in bb:
            cbb += 1
        elif i in mb:
            cmb += 1
    return cmb / cbb
