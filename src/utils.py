import argparse
import glob
import json
import os

import MeCab
import nltk
t = MeCab.Tagger('-Owakati')
sent_detector = nltk.RegexpTokenizer(u'[^　！？。]*[！？。.\n]')


def tokenize(text):
    return t.parse(text).strip()


def split_text(text):
    return sent_detector.tokenize(text)


def list_files(dir_path):
    path = os.path.join(dir_path, '*', 'wiki_*')
    files = glob.glob(path, recursive=True)
    return files


def read_jsonl(filepath):
    with open(filepath) as f:
        for line in f:
            yield json.loads(line)


def extract_text(article):
    return article.get('text', '')


def main(args):
    files = list_files(args.extracted_dir)
    with open(args.save_file, 'w') as f:
        for file in files:
            articles = read_jsonl(file)
            for article in articles:
                text = extract_text(article)
                sents = split_text(text)
                sents = [sent.strip() for sent in sents if sent.strip()]
                text = '\t'.join(tokenize(sent) for sent in sents)
                f.write(f'{text}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Making a dataset.')
    parser.add_argument('--extracted_dir', help='extracted dir by wikiextractor')
    parser.add_argument('--save_file', default='ja.wikipedia.txt', help='filename')
    args = parser.parse_args()
    main(args)
