def reverse_bit(num):
    result = 0
    can_go = True
    prev_num = 0
    while can_go:
        bit = num & 1
        result = (result << 1) | bit
        prev_num = num
        num = num >> 1
        if prev_num == num:
            can_go = False
    return result

if __name__ == "__main__":
    print(reverse_bit(42))
