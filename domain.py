# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import glob


folder = 'templates/'
filename = os.path.join(folder, 'domains.in')
print(filename)
with open(filename, 'r') as myfile:
    soup = BeautifulSoup(myfile.read(), 'html.parser')
    # s = soup.replace(',', ' ')
    # print(s)
# data = []
# for cat in soup.find_all('category'):
#     if cat.parent.name == "topic":
#         continue
#     data += [cat.find("pattern").text]
# print(data)
# data_set = " ".join(data)


# Which media is more suited to learning, movies or books? *
# For me, books are more suited for learning. In enhancing or developing
# your skills in a particular field, you don't watch movie(s) to learn a
# lesson, you read books. Basically, it's because you wanted yourself to
# get nurtured by understanding each modules written on a textbook, like
# formulations, definition of terms, algorithms, logical analytics and
# many more. In movie(s), you can't just deeply absorbed those kind of
# information within just a view on scenario. Reading books, makes you
# more focus and understand each context of a book.

# If your younger sister asked for your opinion about whether she should learn computer science to become a software engineer, how would you respond? *
# If she really wanted to become a software engineer, then I would let her
# learn and study the basic / fundamentals in software engineering like
# algorithms of a particular system, the logical flows, the schema and
# architecture in building a software application.

# What was the last time you had a really, really good time? What did you do? Would you do it again? *
# The time that I learned the basic photography. What I did was, read some articles on the internet, watch videos, then take photos on street, applying all what I've learned from what I had read and watched. And yes, I would do it again, coming back to basic, which will make me more in depth of understanding in photography like setting up your camera on subject you will capture, and organizing the camera's dials:
#     ISO, Aperture, Shutter Speed.

# If you were a fluffy purple elephant, what color would you paint your room? *
# Rose gold


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(4))
