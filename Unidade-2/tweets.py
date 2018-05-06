#coding: utf-8
#Crispiniano
#Unidade 2: Tweets por Página

tweets_pagina = 400

tweets = int(raw_input())

paginas = tweets / tweets_pagina
tweets_perdidos = tweets % tweets_pagina

percentual_tweets_perdidos = 100.0 * tweets_perdidos / tweets

print "Serão necessárias {} página(s) para visualizar os tweets.".format(paginas)
print "{:.1f}% dos tweets serão perdidos.".format(percentual_tweets_perdidos)
