import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

max_results_per_city = 20  # change to get more results

city_set = ["mumbai", "bangalore", "hyderabad", "pune"]

job_title_set = [
    "full+stack+developer",
    "front+end+developer",
    "back+end+developer",
    "software+engineer",
    "data+scientist",
    "machine+learning+engineer",
    "android+developer",
    "ios+developer",
]

columns = ["job_title", "company_name", "summary", "city", "location", "salary", "date"]

sample_df = pd.DataFrame(columns=columns)
for job_title in job_title_set:
    for city in city_set:
        for start in range(0, max_results_per_city, 10):
            url = "http://www.indeed.co.in/jobs?q=%s&l=%s&start=%s" % (
                job_title,
                city,
                start,
            )
            page = requests.get(url)
            print(url)
            time.sleep(1)
            soup = BeautifulSoup(page.text, "lxml", from_encoding="utf-8")
            for div in soup.find_all(name="div", attrs={"class": "row"}):
                # specifying row num for index of job posting in dataframe
                print(job_title + " " + city + " " + str(start))
                print(len(sample_df))
                num = len(sample_df) + 1
                # an empty list to hold the data for each posting
                job_post = []

                # grabbing job title
                try:
                    for a in div.find_all(
                        name="a", attrs={"data-tn-element": "jobTitle"}
                    ):
                        job_post.append(a["title"])
                except:
                    job_post.append("Not Available")

                # grabbing company_name
                try:
                    company = div.find_all(name="span", attrs={"class": "company"})
                    if len(company) > 0:
                        for b in company:
                            job_post.append(b.text.strip())
                    else:
                        sec_try = div.find_all(
                            name="span", attrs={"class": "result-link-source"}
                        )
                        for span in sec_try:
                            job_post.append(span.text)
                except:
                    job_post.append("Not Available")

                # grabbing summary text
                try:
                    d = div.findAll("span", attrs={"class": "summary"})
                    for span in d:
                        job_post.append(span.text.strip())
                except:
                    job_post.append("Not Available")

                # append city name
                job_post.append(city)

                # grabbing location name
                try:
                    c = div.find_all("span", attrs={"class": "location"})
                    for span in c:
                        job_post.append(span.text)
                except:
                    job_post.append("Not Available")

                # grabbing salary
                try:
                    # salary = div.find(name="span",attrs={"class":"no-wrap"})
                    job_post.append(
                        div.find(name="span", attrs={"class": "no-wrap"}).text
                    )
                except:
                    job_post.append("Not Available")

                # grabbing salary
                try:
                    # salary = div.find(name="span",attrs={"class":"no-wrap"})
                    job_post.append(div.find(name="span", attrs={"class": "date"}).text)
                except:
                    job_post.append("Not Available")

                # appending list of job post info to dataframe at index num
                # print(job_post)
                sample_df.loc[num] = job_post


sample_df.to_csv("job_listing.csv", encoding="utf-8")
