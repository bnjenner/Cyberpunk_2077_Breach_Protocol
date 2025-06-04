##########################################################################################


def read_csv(filename):

    result = []

    with open(filename, "r") as file:

        i = 0

        for line in file:

            cols = line.split(",")
            result.append([])

            for c in cols:
                result[i].append(c.strip())

            i += 1

    return result
