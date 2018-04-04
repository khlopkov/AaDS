import random
import string
token = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                for x in range(8))


file = open("input.txt", "w")

for i in range(512):
    token = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                    for x in range(8))
    file.write(token)
    file.write('\n')
file.close()
