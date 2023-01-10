# Compulsory Task 1

# Run all the code extracts in the worksheet

import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)

# Cat and monkey are similar as both are animals
# Monkeys commonly eat bananas, though they aren't similar
# Cat and bananas are not related
# A similar example would be

word1 = nlp("rabbit")
word2 = nlp("dog")
word3 = nlp("carrot")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# When you run the example file with 'en_core_web_sm'
# Similarities are lower and do not seem correct
# You get a message saying "no word vectors are loaded"
# So result is based on "tagger, parser and NER"
# which may not give useful similarity judgements