def twoSum(numbers, target):

    for i in range(len(numbers)):
        potential = i
        for k in range(len(numbers)):
            if ((numbers[k] + numbers[potential]) == target):
                return [numbers[potential], numbers[k]]