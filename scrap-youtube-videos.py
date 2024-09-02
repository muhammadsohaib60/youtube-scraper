
KEYWORDS = [
    'python',
    'django',
    "web3",
    "solidity",
]

# ## How many Videos per keyword?
count = 20  # Set the number of videos you want to retrieve for each keyword

# %%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup Chrome options
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Setup the Chrome WebDriver with the correct arguments
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Function to get the most viral videos for a given keyword
def get_viral_videos(keyword, count):
    query = keyword.replace(' ', '+')
    base_url = f"https://www.youtube.com/results?search_query={query}&sp=CAM%253D"
    driver.get(base_url)
    time.sleep(5)  # Let the page load

    # Scroll down the page to load more results
    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    video_elements = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-video-renderer', href=True)
    title_elements = soup.find_all('yt-formatted-string', class_='style-scope ytd-video-renderer')

    videos = []

    for title_element, video_element in zip(title_elements, video_elements):
        title = title_element.text.strip()
        url = 'https://www.youtube.com' + video_element['href']
        if title and url:  # Ensure both title and url are present
            videos.append({'Keyword': keyword, 'Title': title, 'URL': url})
        if len(videos) >= count:
            break

    return videos

all_videos = []

for keyword in KEYWORDS:
    print(f"\nKeyword: {keyword}")
    videos = get_viral_videos(keyword, count)
    all_videos.extend(videos)

# Create DataFrame
df = pd.DataFrame(all_videos)

# Save DataFrame to CSV
df.to_csv('viral_videos.csv', index=False)
print(f"\nData saved to viral_videos.csv")

driver.quit()  # Close the WebDriver

