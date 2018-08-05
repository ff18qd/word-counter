# word-counter
Python program to count the words in txt file

I used buffer_size when processing file reading to avoid dealing with multi gigabyte files in one process.

For online throughput monitoring the implementaton is based on finishing processing the buffer-size then printing out. It can also apply with time manner. But I haven't get clarification feedback so I leave my solution as it is.

I also request a clarification for definition of word. I make assumption of word is without special characters and separate by whitespaces. If the word can have special charactors the regex part can be removed from process method.
