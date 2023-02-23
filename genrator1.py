def generator(x0, a, m, randomNums, noOfRandomNums):

    randomNums[0] = x0

    for i in range(1, noOfRandomNums):

        randomNums[i] = (a * randomNums[i-1]) % m

    return randomNums

if __name__ == '__main__':

    x0 = 25
    a = 7
    m = 31
    noOfRandomNums = 20

    randomNums = [0] * noOfRandomNums

    generator(x0, a, m, randomNums, noOfRandomNums)

    uniqueNumbers = set()

    for i in randomNums:
        if i in uniqueNumbers:
            print('finish')
            print(uniqueNumbers)
        else:
            uniqueNumbers.add(i)
            print(uniqueNumbers)
            print('not finish')
