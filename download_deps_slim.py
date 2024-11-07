#!/usr/bin/env python3

from huggingface_hub import snapshot_download
import nltk
import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    "https://repo1.maven.org/maven2/org/apache/tika/tika-server-standard/2.6.0/tika-server-standard-2.6.0.jar",
    "http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server-standard/2.6.0/tika-server-standard-2.6.0.jar.md5"
]

repos = [
    "InfiniFlow/text_concat_xgb_v1.0",
    "InfiniFlow/deepdoc",
]

def download_model(repo_id):
    local_dir = os.path.abspath(os.path.join("huggingface.co", repo_id))
    os.makedirs(local_dir, exist_ok=True)
    snapshot_download(repo_id=repo_id, local_dir=local_dir)


if __name__ == "__main__":
    for url in urls:
        filename = url.split("/")[-1]
        print(f"Downloading {url}...")
        if not os.path.exists(filename):
            urllib.request.urlretrieve(url, filename)

    local_dir = os.path.abspath('nltk_data')
    for data in ['wordnet', 'punkt', 'punkt_tab']:
        print(f"Downloading nltk {data}...")
        nltk.download(data, download_dir=local_dir)

    for repo_id in repos:
        print(f"Downloading huggingface repo {repo_id}...")
        download_model(repo_id)
