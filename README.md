# wiki-article-dataset

wiki-article-dataset is a text corpus from the web (japanese wikipedia).

You can download this corpus from the following link:

* [ja.wikipedia_250k.zip](https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/ja.wikipedia_250k.zip)

## Format

Each line represents an article and it contains sentences divided by <tab>:

```python
word_1 word_2 ... word_k <tab> ... <tab> word_n
... 
```


## Requirements

* Python 3.6+
* MeCab
* pipenv

## Make corpus by yourself

You can download this corpus. But you can make the corpus by yourself.

Simply run:

```commandline
$ ./build.sh
```
