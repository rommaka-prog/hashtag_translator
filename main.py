from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= "pt ", target= " en")

texto = "Fala pessoal, inscrevam-se no canal do YouTube para aprenderem mais sobre programação em Python e outras linguagens de programação. "

traducao = tradutor.translate(texto)
print(traducao)
