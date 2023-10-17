import sys
import datetime

from gensim.corpora import WikiCorpus


def wiki2txt(articles_data_path):
    wiki_corpus = WikiCorpus(articles_data_path, dictionary={}, processes=16)

    with open("articles_texts.txt", "w", encoding="utf-8", buffering=4096) as f:
        num = 0
        wait_to_write = []
        for text in wiki_corpus.get_texts():
            wait_to_write.append(" ".join(text) + "\n")
            num += 1
            if num % 10000 == 0:
                f.writelines(wait_to_write)
                wait_to_write.clear()
                print(f"{datetime.datetime.now().strftime("%H:%M:%S.%f")} 处理了 {num} 个条目")
    print("处理完成")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} path/to/wiki_articles_data")
        exit()
    wiki2txt(sys.argv[1])
