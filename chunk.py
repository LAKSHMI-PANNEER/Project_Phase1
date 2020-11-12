import nltk.tokenize as nt
import nltk

text="Tap the watch screen to bring up your apps. Swipe down and tap Bluetooth. Tap the switch to turn Bluetooth on. "

ss=nt.sent_tokenize(text)
tokenized_sent=[nt.word_tokenize(sent) for sent in ss]

pos_sentences=[nltk.pos_tag(sent) for sent in tokenized_sent]
p=pos_sentences
#print(p)

def extract_NN(sent):
    grammar = r"""
    NBAR:
        # Nouns and Adjectives, terminated with Nouns
        {<NN.*>*<NN.*>}

    NP:
        {<NBAR>}
        # Above, connected with in/of/etc...
        {<NBAR><IN><NBAR>}
    """
    chunker = nltk.RegexpParser(grammar)
    ne = set()
    chunk = chunker.parse(nltk.pos_tag(nltk.word_tokenize(sent)))
    for tree in chunk.subtrees(filter=lambda t: t.label() == 'NP'):
        ne.add(' '.join([child[0] for child in tree.leaves()]))
    return ne

n=extract_NN(text)
print("Objects:",n)
