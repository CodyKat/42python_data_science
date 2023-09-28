def ft_tqdm(lst):
    ret = 0
    for i in lst:
        i = i + 1
        bar = ""
        percent = int(ret * 100 / len(lst))
        for j in range(int(percent / 1.5625)):
            if j == int(percent / 1.5625) - 1:
                bar += '>'
            else:
                bar += '='
        print("\r%3d%%|[%-64s]| %d/%d" % (percent, bar, ret, len(lst)), end="")
        yield ret
        ret += 1
