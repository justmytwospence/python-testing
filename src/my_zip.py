def my_zip(*iterables):
    i = 0
    stop = False
    while not stop:
        output = []
        for iterable in iterables:
            try:
                output.append(iterable[i])
            except IndexError:
                stop = True
        if len(output) == len(iterables):
            yield tuple(output)
        i += 1
