from collections import Counter

# cube root of the fractinal part of first 64 prime numbers in binary of 32 bit length
K_CONSTANTS: list[str] = [
    "01000010100010100010111110011000",
    "01110001001101110100010010010001",
    "10110101110000001111101111001111",
    "11101001101101011101101110100101",
    "00111001010101101100001001011011",
    "01011001111100010001000111110001",
    "10010010001111111000001010100100",
    "10101011000111000101111011010101",
    "11011000000001111010101010011000",
    "00010010100000110101101100000001",
    "00100100001100011000010110111110",
    "01010101000011000111110111000011",
    "01110010101111100101110101110100",
    "10000000110111101011000111111110",
    "10011011110111000000011010100111",
    "11000001100110111111000101110100",
    "11100100100110110110100111000001",
    "11101111101111100100011110000110",
    "00001111110000011001110111000110",
    "00100100000011001010000111001100",
    "00101101111010010010110001101111",
    "01001010011101001000010010101010",
    "01011100101100001010100111011100",
    "01110110111110011000100011011010",
    "10011000001111100101000101010010",
    "10101000001100011100011001101101",
    "10110000000000110010011111001000",
    "10111111010110010111111111000111",
    "11000110111000000000101111110011",
    "11010101101001111001000101000111",
    "00000110110010100110001101010001",
    "00010100001010010010100101100111",
    "00100111101101110000101010000101",
    "00101110000110110010000100111000",
    "01001101001011000110110111111100",
    "01010011001110000000110100010011",
    "01100101000010100111001101010100",
    "01110110011010100000101010111011",
    "10000001110000101100100100101110",
    "10010010011100100010110010000101",
    "10100010101111111110100010100001",
    "10101000000110100110011001001011",
    "11000010010010111000101101110000",
    "11000111011011000101000110100011",
    "11010001100100101110100000011001",
    "11010110100110010000011000100100",
    "11110100000011100011010110000101",
    "00010000011010101010000001110000",
    "00011001101001001100000100010110",
    "00011110001101110110110000001000",
    "00100111010010000111011101001100",
    "00110100101100001011110010110101",
    "00111001000111000000110010110011",
    "01001110110110001010101001001010",
    "01011011100111001100101001001111",
    "01101000001011100110111111110011",
    "01110100100011111000001011101110",
    "01111000101001010110001101101111",
    "10000100110010000111100000010100",
    "10001100110001110000001000001000",
    "10010000101111101111111111111010",
    "10100100010100000110110011101011",
    "10111110111110011010001111110111",
    "11000110011100010111100011110010",
]

# square roots of the fractional part of first 8 prime numbers in binary in 32 bnit length
HASH_CONSTANTS: list[str] = [
    "01101010000010011110011001100111",
    "10111011011001111010111010000101",
    "00111100011011101111001101110010",
    "10100101010011111111010100111010",
    "01010001000011100101001001111111",
    "10011011000001010110100010001100",
    "00011111100000111101100110101011",
    "01011011111000001100110100011001",
]


def b2hexa(binary: str) -> str:
    decimal = b2d(binary)
    h = ""
    # hexa: list[str] = []
    while decimal != 0:
        temp = decimal % 16
        if temp < 10:
            h = str(temp) + h
            # hexa.insert(0, str(temp))
        else:
            h = chr(temp + 55) + h
            # hexa.insert(0, chr(temp + 55))
        decimal = int(decimal / 16)
    print(f"binary2hexa = {h}\t{len(h)}", file=log_file)
    return h


def f2b(frac: float, k_prec: int = 32) -> str:
    """Gives binary of floating point numbers between 0 and 1

    Args:
        frac (float): number between 0 and 1
        k_prec (int, optional): desired length of binary number. Defaults to 32.

    Returns:
        str: Binary in string
    """
    binary = ""
    while k_prec:
        # Find next bit in fraction
        frac *= 2
        fract_bit = int(frac)

        if fract_bit == 1:

            frac -= fract_bit
            binary += "1"

        else:
            binary += "0"

        k_prec -= 1
    print(f"fraction2binary = {binary}\t{len(binary)}", file=log_file)
    return binary


def d2b(num: int, l: int = 32) -> str:
    """Decimal to Binary

    Args:
        num (int): number to be converted

    Returns:
        str: Binary in string format
    """
    original = num
    binary: list[int] = []
    binstr: str = ""
    while num >= 1:
        binary.insert(0, num % 2)
        num = int(num / 2)
    for i in binary:
        binstr += str(i)

    binstr = binstr.rjust(l, "0")

    # return binary
    print(f"d2b({original}) = {binstr}\t{len(binstr)}", file=log_file)
    return binstr


def rotr(bit: str, n: int) -> str:
    """Right Rotates the 32 bit block by given number n

    Args:
        bit (str): bit to be rotated
        n (int): rotate by number

    Returns:
        str: rotated bit
    """
    res = ""
    if n == 32:
        print(bit)
        return bit
    elif n < 32:
        bitlist = list(bit)
        for _ in range(n):
            bitlist.insert(0, bitlist[-1])
            bitlist.pop()
    else:
        n = n % 32
        bitlist = list(bit)
        for _ in range(n):
            bitlist.insert(0, bitlist[-1])
            bitlist.pop()
    for b in bitlist:
        res += b
    print(f"rightrot. by {n} = {bit} -> {res}\t{len(res)}", file=log_file)
    return res


def xor(bit1: str, bit2: str) -> str:
    result = ""
    if len(bit1) != len(bit2):
        min(bit1, bit2, key=len).rjust(len(max(bit1, bit2, key=len)), "0")

    for bit in range(len(bit1)):
        if bit1[bit] == bit2[bit]:
            result = result + "0"
        else:
            result = result + "1"
    print(f"xor -\n{bit1}\n{bit2}\n----\n{result}\t{len(result)}", file=log_file)
    return result


def shiftR(bit: str, n: int) -> str:
    shifted = bit[0 : (len(bit) - n)]
    s = shifted.rjust(len(bit), "0")
    print(f"shiftR of \n{bit} by {n} bits\n---\n{s}\t{len(s)}", file=log_file)
    return s


def b2d(binarystr: str) -> int:
    decimal = 0
    i = 0
    while len(binarystr) >= 1:
        base = int(binarystr[-1])
        decimal += pow(2, i) * base
        i += 1
        binarystr = binarystr[:-1]
    print(f"binary2deci = {decimal}", file=log_file)
    return decimal


def addition(n1: str, n2: str) -> str:
    dn1 = b2d(n1)
    dn2 = b2d(n2)
    result = (dn1 + dn2) % 2**32
    addi = d2b(result).rjust(len(n1), "0")
    print(f"\naddition --\n{n1}\n{n2}\n-----\n{addi}\t{len(addi)}", file=log_file)
    return addi


def sigma0(bit: str) -> str:
    temp: str = xor(rotr(bit, 7), rotr(bit, 18))
    res: str = xor(temp, shiftR(bit, 3))
    print(f"sig0 = {res}\t{len(res)}", file=log_file)
    return res


def sigma1(bit: str) -> str:
    temp: str = xor(rotr(bit, 17), rotr(bit, 19))
    res: str = xor(temp, shiftR(bit, 10))
    print(f"sig1 = {res}\t{len(res)}", file=log_file)
    return res


def capsig0(bits: str) -> str:
    rot1 = rotr(bits, 7)
    rot2 = rotr(bits, 22)
    rot3 = rotr(bits, 13)
    temp = xor(rot1, rot2)
    result = xor(temp, rot3)
    print(f"csig0 = {result}\t{len(result)}", file=log_file)
    return result


def capsig1(bits: str) -> str:
    rot1 = rotr(bits, 6)
    rot2 = rotr(bits, 11)
    rot3 = rotr(bits, 22)
    temp = xor(rot1, rot2)
    result = xor(temp, rot3)
    print(f"csig1 = {result}\t{len(result)}", file=log_file)
    return result


def choice(x: str, y: str, z: str) -> str:
    result: str = ""
    for i in range(len(x)):
        if x[i] == "1":
            result += y[i]
        elif x[i] == "0":
            result += z[i]
    print(f"choice b/w\n{x}\n{y}\n{z}\n-----\n{result}\t{len(result)}", file=log_file)
    return result


def majority(x: str, y: str, z: str) -> str:
    maj: str = ""
    for i in range(len(x)):
        l = list(x[i] + y[i] + z[i])
        oc = Counter(l)
        majority = oc.most_common(1)[0][0]
        if majority == "1":
            maj += "1"
        else:
            maj += "0"
    print(f"majority b/w\n{x}\n{y}\n{z}\n----\n{maj}\t{len(maj)}", file=log_file)
    return maj


def msgshd(block: str) -> list[str]:
    msw: list[str] = []
    # dividing the msg block into schedules
    for i in range(16):
        msw.append(block[32 * i : (32 * (i + 1))])
    # adding rest of the message schedules up-to 64
    for t in range(16, 64):
        temp1 = addition(msw[t - 16], sigma0(msw[t - 15]))
        temp2 = addition(temp1, msw[t - 7])
        temp3 = addition(temp2, sigma1(msw[t - 2]))
        msw.append(temp3)
    for i in range(len(msw)):
        print(f"msg schedule {i} = {msw[i]}", file=log_file)
    return msw


def temp1(k: str, w: str, initial_hash: list[str]) -> str:
    add1 = addition(
        capsig1(initial_hash[5]),
        choice(initial_hash[4], initial_hash[5], initial_hash[6]),
    )
    add2 = addition(initial_hash[7], k)
    add3 = addition(add1, add2)
    add4 = addition(add3, w)
    return add4


def temp2(hv: list[str]) -> str:
    add1 = addition(capsig0(hv[0]), majority(hv[0], hv[1], hv[2]))
    return add1


# def compression(sch:list[str], hash:list[str]) -> list[str]:


def hash(s: str) -> str:
    print(f"string = {s}", file=log_file)
    hdigest = ""
    initial_hash = list(HASH_CONSTANTS)
    # convert to ascii ord()
    o: list[int] = [ord(x) for x in s]
    print(f"ord = {o}", file=log_file)
    bxmsg: str = ""

    # convert to binary and concatenate
    for i in o:
        bxmsg += d2b(i, 8)

    # len of original message in binary of 64 bit length
    msglen: str = d2b(len(bxmsg)).rjust(64, "0")

    # Add 1 to right
    bxmsg += "1"

    # calculating number of msg blocks needed
    n = 0
    while True:
        if len(bxmsg) * n < n * (512 * n - 64):
            break
        n += 1

    # padding to n message blocks of 512 bit length
    paddedmsg: str = bxmsg.ljust(512 * n - 64, "0") + msglen

    print(f"msg = {paddedmsg}\t{len(paddedmsg)}", file=log_file)

    # creating required message blocks
    msgblocks: list[str] = []
    for i in range(n):
        msgblocks.append(paddedmsg[(512 * i) : (512 * (i + 1))])

    # Creating message scedule for each block
    for block in msgblocks:
        msgschedule = msgshd(block)

        # calculating temporary values
        for i in range(len(msgschedule)):
            print(f"msgsch ={msgschedule[i]}\t{len(msgschedule[i])}", file=log_file)
            k: str = K_CONSTANTS[i]
            w: str = msgschedule[i]
            t1 = temp1(k, w, initial_hash)
            t2 = temp2(initial_hash)
            a = addition(t1, t2)

            # computing hash values and compressing
            initial_hash.insert(0, a)
            initial_hash.pop()
            b = addition(initial_hash[4], t1)
            initial_hash[4] = b

        # adding initial hash values into initial_hash
        for i in range(len(HASH_CONSTANTS)):
            initial_hash[i] = addition(initial_hash[i], HASH_CONSTANTS[i])
    for d in initial_hash:
        hdigest += b2hexa(d)
    return hdigest


# FIXME: Wrong msg schedule generating


if __name__ == "__main__":
    ########################################
    log_file = open("log.txt", "w")
    ######################################
    h = hash("abc")  # BA7816BF8F01CFEA414140DE5DAE2223B00361A396177A9CB410FF61F20015AD
    print(
        h,
        len(h),
    )
    ######################################
    log_file.close()
    ######################################
# pass
