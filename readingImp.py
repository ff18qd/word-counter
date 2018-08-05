import re
from collections import OrderedDict
import codecs


def process(line, wordcount):
    for word in line.split():
        # remove special signs other than alphabetic and numeric
        word = re.sub(r'[\W_]+', '', word)
        if word not in wordcount:
            # re.sub(r'[\W_]+', '', word)
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        print("current throughput", len(line))


def wordCount(path, buffer_size):
    # utf-8-sig to handle bom
    file = codecs.open(path, mode="r", encoding='utf-8-sig')
    wordcount = {}
    # every time read up to buffer sized lines of text
    # to avoid load everything to memory
    lines = file.readlines(buffer_size)
    while lines:
        for line in lines:
            process(line, wordcount)
        lines = file.readlines(buffer_size)

    file.close()

    d_sorted_by_value = OrderedDict(sorted(wordcount.items(), key=lambda x: x[1], reverse=True))
    # in a descending pattern
    for k, v in d_sorted_by_value.items():
        print(k, v)


wordCount("./short-story.txt", 1024)