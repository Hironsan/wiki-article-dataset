import json
import os
import random
from itertools import chain
from keras.preprocessing.text import Tokenizer


def load_articles(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()


def split_sents(article):
    return [sent.split(' ') for sent in article.split('\t')]


def build_vocab(sents):
    tok = Tokenizer(oov_token='<UNK>', filters='')
    tok.fit_on_texts(sents)
    return tok


def generate_positive_pairs_from_single_article(sents, tokenizer):
    idx = random.randrange(0, len(sents))
    center = sents.pop(idx)
    wrapper_tokens = tokenizer.texts_to_sequences(sents)
    sent_tokens = tokenizer.texts_to_sequences([center])
    yield {'in0': sent_tokens, 'in1': wrapper_tokens, 'label': 1}


def generate_positive_pairs_from_single_file(sents_per_article, tokenizer):
    iter_list = [generate_positive_pairs_from_single_article(sents, tokenizer)
                 for sents in sents_per_article
                 ]
    return chain.from_iterable(iter_list)


if __name__ == '__main__':
    filepath = 'ja.wikipedia_250k.txt'
    datadir = '.'
    articles = load_articles(filepath)
    sents_per_article = [split_sents(a) for a in articles]
    sents = chain(*sents_per_article)
    tokenizer = build_vocab(sents)
    sents = tokenizer.texts_to_sequences(sents)
    train_prefix = 'train250k'
    fname = "wikipedia_{}.txt".format(train_prefix)
    outfname = os.path.join(datadir, '{}_tokenized.jsonl'.format(train_prefix))
    with open(outfname, 'w') as f:
        for sample in generate_positive_pairs_from_single_file(sents_per_article, tokenizer):
            f.write('{}\n'.format(json.dumps(sample)))
