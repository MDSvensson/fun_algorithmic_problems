import re


def wordcount_1():
    string = input("Enter text:")
    words = re.findall(r"[A-z]+", string.lower())
    print(words)
    print(len(words))
    return len(words)


def wordcount_2(stopwords):
    with open("stopwords.txt", "r") as file:
        stopwords = file.read()
        stopwords = stopwords.replace("\n", " ").split()
        string = input("Enter text:")
        words = re.findall(r"[A-z]+", string.lower())
        bow = [b for b in words if all(a not in b for a in stopwords)]
        print(bow)
        print(len(words))
        return len(words)


import sys


def wordcount_3():
    try:
        with open("mytext.txt", "r") as file:
            string = file.read()
            string = string.replace("\n", " ")
    except:
        string = input("Enter string:")
        string = string.replace("\n", " ")

    with open("stopwords.txt", "r") as file:
        stopwords = file.read()
        stopwords = stopwords.replace("\n", " ").split()
    words = re.findall(r"[A-z]+", string.lower())
    bow = [b for b in words if all(a not in b for a in stopwords)]
    print(bow)
    print(len(bow))
    print(stopwords)
    print(len(stopwords))
    return len(bow)


def wordcount_5():
    try:
        with open("mytext.txt", "r") as file:
            string = file.read().replace("\n", " ")
    except:
        string = input("Please input a string:").replace("\n", " ")

    with open("stopwords.txt", "r") as file:
        stopwords = file.read()
        stopwords = stopwords.replace("\n", " ").split()

    words = re.findall(r"\-??[A-zçã]+\-?[A-zçã]+", string.lower())
    bow = filter(lambda x: x not in stopwords, words)
    res = list(bow)
    print(res, "\n", len(res))
    return res


if __name__ == "__main__":
    wordcount_5()
