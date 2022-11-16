# Vividly Takehome - Andreas Lordos
Web scraper to extract files of a given type 
## Usage
```
pip install -r requirements.txt
python3 vividly_takehome.py -l https://cms.math.ca/competitions/cmo/ -f  "Math Problems"
```
## Docs
Argument | Usage | Default | Required |
--- | --- | --- | --- |
-l, --link | Site URL to scrape | - | Yes | 
-ft, --filetype | Set filetype to download | pdf | No
--quiet | Do not display download progress |False| No
--save-here | Save files in current directory | False | No
-f, --save-path | Save files in the provided folder | ~/Downloads/ | No

