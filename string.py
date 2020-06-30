from fuzzywuzzy import fuzz

# Juan Enrique de Luna Diaz
# Juan E. Luna Diaz

# calcula a similaridade da string em ordem
fuzz.ratio('Apple Inc.', 'Apple')

# Similaridade da string PARCIAL
fuzz.ratio('Apple Inc.', 'Apple')
fuzz.partial_ratio('Apple Inc.', 'Apple') #elas são 100% parecidas

# Ignora a ordem das palavras
fuzz.ratio('Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.partial_ratio('Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.token_sort_ratio('Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')

# Ignora palavras duplicadas - tem tendencia a dar melhor resultado
fuzz.ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.partial_ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.token_sort_ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.token_set_ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
