import string
import random


def generateOTP() -> int:
    generate_otp: str = ""
    digits: str = "0123456789"
    for _ in range(4):
        generate_otp = generate_otp + random.choice(digits)
    otp: int = int(generate_otp)
    return otp


def encrypt(s: str) -> str:
    e = ""
    str = list(string.ascii_letters + string.digits + "!^&*()+/:;',.?><@#$%_- ")
    kstr = list(string.ascii_letters + string.digits + "!^&*()+/:;',.?><@#$%_- ")
    key = generateOTP()
    random.seed(key)
    print(f"key is {key}")
    random.shuffle(kstr)
    for i in range(len(s)):
        idx = str.index(s[i])
        e += kstr[idx]
    return e


def decrypt(s: str, k: int) -> str:
    d = ""
    str = list(string.ascii_letters + string.digits + "!^&*()+/:;',.?><@#$%_- ")
    kstr = list(string.ascii_letters + string.digits + "!^&*()+/:;',.?><@#$%_- ")
    random.seed(k)
    random.shuffle(kstr)
    for i in range(len(s)):
        idx = kstr.index(s[i])
        d += str[idx]
    return d


if __name__ == "__main__":
    print(encrypt("Hello World"))
    print(decrypt(input("msg: "), int(input("key: "))))
