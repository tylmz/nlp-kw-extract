from __future__ import absolute_import
from __future__ import print_function
import six
import rake
import operator
import io

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = io.open("test/a1.txt", 'r',encoding="UTF-8")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Keywords:", keywords)

print("----------")
# 1. Split text into sentences
sentenceList = rake.split_sentences(text)

for sentence in sentenceList:
    print("Sentence:", sentence)
