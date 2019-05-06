pipenv install
git clone https://github.com/attardi/wikiextractor.git

wget https://dumps.wikimedia.org/jawiki/20181220/jawiki-20181220-pages-articles.xml.bz2
python wikiextractor/WikiExtractor.py -o extracted --json jawiki-20181220-pages-articles.xml.bz2
python src/utils.py --extracted_dir=extracted
