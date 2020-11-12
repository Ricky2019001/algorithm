def reverseWords(str):
    return " ".join(str.split()[::-1])


if __name__ == '__main__':
    str = "the sky is blue"
    print(reverseWords(str))
