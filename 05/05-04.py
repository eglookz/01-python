from translate import Translator

translator = Translator(to_lang='ru')
with open('05-04.txt', 'r') as f:
  translated = []
  lines = f.read().split('\n')

  with open('05-04-out.txt', 'w') as fout:
    for line in lines:
      words = line.split()
      translation = translator.translate(words[0])
      print(translation, words[1], words[2], file=fout)
