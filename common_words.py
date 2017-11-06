import re
from collections import Counter
from itertools import islice, izip, tee

with open("trump_tweets_text.txt", "r") as fobj:
    tweets = fobj.read().lower()

#remove articles, conjuctions, prepositions, etc.
remove_words = ['because','android','about','below','excepting','off','toward','above','beneath','for','on','under','across','beside','besides','from','onto','underneath','after','between','in','out','until','against','beyond','in front of','outside','up','along','but','inside','over','upon','among','by','in spite of','past','up to','around','concerning','instead of','regarding','with','at','despite','into','since','within','because of','down','like','through','without','before','during','near','throughout','with regard to','behind','except','of','to','with respect to','for','and','but','nor','or','yet','so','the','a','an','her','his','each','some','both','all','that','those','this','there','when','where','why','how','which','RT','will','be','the','android','client','web','not','if','am','are','were']

remove = '|'.join(remove_words)
regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
clean_text = regex.sub("", tweets)

words = re.findall("\w+",
      clean_text)

#changing value of n determines how many words to look for
def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break

word_count = Counter(ngrams(words, 2))

print word_count.most_common(100)
