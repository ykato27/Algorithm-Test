def average_words_lenghts_v1(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, "")
    words = sentence.split()
    sum = 0

    for word in words:
        sum += len(word)

    return round(sum / len(words), 2)


def average_words_lenghts_v2(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, "")
    words = sentence.split()
    return round(sum(len(word) for word in words) / len(words), 2)


# mapメソッドを使う方法
def average_words_lenghts_v3(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, "")
    words = sentence.split()
    return round(sum(map(len, words)) / len(words), 2)


if __name__ == "__main__":
    sentence1 = "Hi all, my name is Tom...I am originally from Australia."
    sentence2 = "I need to work very hard to learn more about algorithms in Python!"

    print(average_words_lenghts_v1(sentence1))
    print(average_words_lenghts_v1(sentence2))

    print(average_words_lenghts_v2(sentence1))
    print(average_words_lenghts_v2(sentence2))

    print(average_words_lenghts_v3(sentence1))
    print(average_words_lenghts_v3(sentence2))
