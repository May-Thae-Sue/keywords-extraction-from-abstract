# keywords-extraction-from-abstract
example.py program file extracts keywords from the input abstract. 
It extracts keywords such as Noun and Adjectives. 
nltk dataset is used to tag the abstract.
The input file must be json which stores the title as the name and the abstrct as the value. example.py output the json output which hold the title as the name and extracted keyword array as the value. 

e.g. {"[u'neural machine translation for low resource languages using bilingual lexicon induced from comparable corpora": ["[", "u'resources", "non-english", "languages", "scarce", "paper", "problem", "context", "machine", "translation", "parallel", "sentence", "pairs", "multilingual", "articles", "available", "internet", "paper", "end-to-end", "siamese", "bidirectional", "recurrent", "neural", "network", "parallel", "sentences", "comparable", "multilingual", "articles", "wikipedia", "dataset", "bleu", "scores", "nmt", "phrase-based", "smt", "systems", "low-resource", "language", "pairs", "english\\u2013hindi", "english\\u2013tamil", "limited", "bilingual", "corpora", "language", "pairs"]}
