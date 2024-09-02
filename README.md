
## Youtube Video Scraper

open up terminal. make sure you have python installed.

in terminal write this command: "pip install requests beautifulsoup4"

once that is installed. you can run the python file: scrap-youtube-videos.py
it will give you a csv with the desired titles and urls of the top videos related to the keywords.

if you want to change the count or the keywords, you can change them by changing these two variables:

list of keywords:
KEYWORDS = [
'python',
'django',
"web3",
"solidity",
]

and

count = 20 # Set the number of videos you want to retrieve for each keyword
