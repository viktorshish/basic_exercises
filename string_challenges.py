# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'.lower()
count_a = word.count('а')
print(count_a)


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
vowels = 'аеёиоуыэюя'
count_vowels = 0
for letter in word:
    if letter in vowels:
        count_vowels += 1
print(count_vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list = sentence.split(' ')
for word in sentence_list:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_list = sentence.split(' ')
count_letters = 0
for word in sentence_list:
    count_letters += len(word)
print(count_letters // len(sentence_list))
