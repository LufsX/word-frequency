import datetime
import multiprocessing

from count import count_large_file as count
from download import download_file
from preprocessing import process_large_file as preprocess
from segment import process_segment_large_file as segment
from wiki2txt import wiki2txt

if __name__ == "__main__":
    multiprocessing.freeze_support()

    proxied = True
    source_link = (
        "https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2"
    )

    start_time = datetime.datetime.now()
    date = start_time.strftime("%Y%m%d")

    source_file = "zhwiki-latest-pages-articles.xml.bz2"
    text_file = f"zhwiki_{date}.txt"
    pre_file = f"zhwiki_{date}.pre.txt"
    seg_file = f"zhwiki_{date}.seg.txt"
    count_file = f"zhwiki_{date}.count.txt"

    download_file(source_link, source_file, proxied=proxied)
    wiki2txt(source_file, text_file)
    preprocess(text_file, pre_file)
    segment(pre_file, seg_file)
    count(seg_file, count_file)

    end_time = datetime.datetime.now()
    print(f"执行完毕，总共耗时 {end_time - start_time}")
