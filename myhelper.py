def count_indians(how_many_rounds):
    for round in range(how_many_rounds):
        x_little = ["{} little".format((3 * round) + x) for x in [1, 2, 3]]
        line = "%s indians" % ' '.join(x_little)
        print(line)
