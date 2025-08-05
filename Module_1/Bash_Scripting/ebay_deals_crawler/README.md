## Introduction
This module shows how to crawl data from [Ebay Daily Deals](https://www.ebay.com/globaldeals/fashion/handbags-and-accessories)

![Ebay Daily Deals](imgs/deals.png)

## How-to Guide
```shell
conda activate crawler
pip install -r requirements.txt
python main.py
```
The crawled data will be stored in the `data` directory

## TODO
- Investigate the bug `Either image's URL or product name can not be found, skipped!`