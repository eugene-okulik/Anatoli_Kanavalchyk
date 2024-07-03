"""Работа с текстом."""


text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
       "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

modified_text = ' '.join([word[:-1] + 'ing' + word[-1]
                          if word[-1] in ',.'
                          else word + 'ing'
                          for word in text.split()])


print(modified_text)
