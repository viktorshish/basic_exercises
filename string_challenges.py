# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюя'
count = 1
for letter in word:
    if letter in vowels:
        count += 1
print(count)


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
count_word = 0
count_letters = 0
for word in sentence_list:
    count_word += 1
    count_letters += len(word)
print(int(count_letters/count_word))
