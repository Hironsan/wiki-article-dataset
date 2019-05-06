# wiki-article-dataset

wiki-article-dataset is a text corpus generated from japanese wikipedia(20181220 dump).

You can download this corpus from the following link:

* [ja.wikipedia_250k.zip](https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/ja.wikipedia_250k.zip)

## Format

Each line represents an article and it contains sentences divided by tab:

```python
ニューヨーク 市 の 建築 ニューヨーク 市 の 建築 ...<tab>
...
```

Each sentence is tokenized by MeCab and IPADIC.

## Example use cases

### Learning Sentence Embeddings

Learning the mapping between sentences. Given the embedding of one sentence, one can find semantically similar/relevant sentences.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2018/11/07/ss1.gif)

Ref: <https://aws.amazon.com/blogs/machine-learning/introduction-to-amazon-sagemaker-object2vec/>

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
