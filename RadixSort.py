def radix_sort(list1):
    if len(list1) is not 0:
        maxItem = max(list1)
        iteration = 0
        result = list1
        while maxItem > 10**iteration:
            result = get_numbers(sortToBuckets(result, iteration))
            iteration += 1
    else:
        result = []
    return result


def sortToBuckets(list1, iteration):
    bins = [[], [], [], [], [], [], [], [], [], []]
    for number in list1:
        digit = (number // (10 ** iteration)) % 10
        bins[digit].append(number)
    return bins


def get_numbers(bins):
    numbers = []
    for bin_item in bins:
        for number in bin_item:
            numbers.append(number)
    return numbers