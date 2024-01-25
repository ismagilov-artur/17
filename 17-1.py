def parrot(phrase):
    if phrase in data:
        print(phrase)
    else:
        data.add(phrase)


data = set()
parrot('Привет!')
parrot('Привет!')
parrot('Как дела?')