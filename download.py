import requests
import os
import datetime


def download_file(url, file_path, proxied=False):
    if proxied:
        url = "https://cors.isteed.cc/" + url
    if os.path.exists(file_path):
        print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} {file_path} 已存在，跳过下载")
        return
    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 开始下载 {url}")
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)
    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 下载完成，已保存至 {file_path}")


if __name__ == "__main__":
    proxied = True
    url = (
        "https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2"
    )
    file_path = "zhwiki-latest-pages-articles.xml.bz2"

    download_file(url, file_path, proxied=proxied)
