import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# Baixar o recurso necessário (uma vez apenas)
nltk.download('punkt_tab')
# Texto de exemplo
texto = "A tokenização é uma parte essencial do processamento de texto."
# Tokenização de palavras
tokens_palavras = word_tokenize(texto)
# Tokenização de frases
tokens_frases = sent_tokenize(texto)
# Tokenização de caracteres
tokens_caracteres = list(texto)
# Exibir resultados
print("Tokens de palavras:", tokens_palavras)
print("Tokens de frases:", tokens_frases)
print("Tokens de caracteres:", tokens_caracteres)
