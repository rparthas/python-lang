def reverse_bits(num):
    result = 0
    while num > 0:
        bit = num & 1
        print(bit,(result << 1),(result << 1) | bit)
        result = (result << 1) | bit
        num = num >> 1
    return result

if __name__ == "__main__":
    print(reverse_bits(33))
