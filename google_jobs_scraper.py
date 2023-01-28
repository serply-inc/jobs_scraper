import requests
from bs4 import BeautifulSoup

keywords = "nurse+work+from+home"

# build the url
URL = f"https://www.google.com/search?q={keywords}&ibp=htl;jobs"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

# make the request to get html
resp = requests.get(URL, headers=headers)
html = resp.content

# create a results variable to save the values
results = {"jobs": []}

# load the html into beautiful soup
soup = BeautifulSoup(html, "lxml")

# grab the job list
job_list_div = soup.find('div', {"aria-label": "Jobs list"})
# grab the un ordered list
job_ul = job_list_div.find('ul')
# get all the list items
job_list_items = job_ul.find_all('li', recursive=False)

# parse each list item
for job_list_item in job_list_items:
    job = {
        "perks": [],
        "position": job_list_item.find("h2").text
    }

    # grab the job title
    job["position"] = job_list_item.find("h2").text

    # get div with company name
    company_div = job_list_item.find("div", {"class": "vNEEBe"})
    job["company"] = company_div.text

    # get div with location
    location_div = job_list_item.find("div", {"class": "Qk80Jf"})
    job["location"] = location_div.text

    # get perks
    perks_divs = job_list_item.find_all("div", {"class": "I2Cbhb"})
    for perks_div in perks_divs:
        job["perks"].append(perks_div.text)

    print(job)
    # save the job into results
    results["jobs"].append(job)

