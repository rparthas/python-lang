def hamming(num):
    print(num)
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num%2 == 0:
        return hamming(int(num/2))
    return 1+hamming(int(num/2))

if __name__ == "__main__":
    print(hamming(157))
