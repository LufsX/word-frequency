import datetime
import sys

from gensim.corpora import WikiCorpus


def wiki2txt(articles_data_path, output_file_path):
    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 开始将 {articles_data_path} 文件转换为纯文本文件"
    )
    wiki_corpus = WikiCorpus(articles_data_path, dictionary={})

    with open(output_file_path, "w", encoding="utf-8", buffering=4096) as f:
        num = 0
        wait_to_write = []
        for text in wiki_corpus.get_texts():
            wait_to_write.append(" ".join(text) + "\n")
            num += 1
            if num % 10000 == 0:
                f.writelines(wait_to_write)
                wait_to_write.clear()
                print(
                    f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 处理了 {num} 个条目"
                )
        if wait_to_write:
            f.writelines(wait_to_write)
            wait_to_write.clear()
    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 保存到 {output_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            f"Usage: python3 {sys.argv[0]} path/to/wiki_articles_data path/to/output_file"
        )
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    wiki2txt(input_file, output_file)
