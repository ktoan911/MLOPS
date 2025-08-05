#!/bin/bash
python3 -m venv myenv
source myenv/bin/activate
pip3 install pandas
cd /home/quandv/Documents/fsds/m1/bash_scripting/scripts/cronjob
python3 crawl.py