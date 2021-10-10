from collections import Counter
from Messages.Processed import *

target = "BEMBOL"

with open(f"/home/ubuntu/PycharmProjects/Youtube-Ai/Messages/{target}.txt") as input_file:

    count = Counter(word for line in input_file
                    for word in line.split())
    c = count.most_common()

    with open(f"/home/ubuntu/PycharmProjects/Youtube-Ai/Messages/Processed/{target}.txt", "w") as write_file:
        for x in c:
            if x[1] >= 1:
                print(x)
                write_file.write(str(x)+"\n")





