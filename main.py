import pandas
from fuzzywuzzy import fuzz, process
import Levenshtein

#TODO: Ask a user to insert the domain name
uk_domain_name = "https://www.samsung.com/uk/"
us_domain_name = "https://www.samsung.com/us/"

us_data = pandas.read_csv("Samsung US.csv")
uk_data = pandas.read_csv("Samsung UK.csv")

full_us_list = us_data["URL"].to_list()
us_list = [x.replace(us_domain_name, "") for x in full_us_list]

full_uk_list = uk_data["URL"].to_list()
uk_list = [x.replace(uk_domain_name, "") for x in full_uk_list]

#TODO: ADD IF THERE IS A 100% MATCH, THEN WE DO NOT NEED OTHER VARIANTS

result = {"UK_URL": [],
          "US_Match_URL": [],
          "Similarity": [],
          }

#fuzz.ratio is better for comparison - gives numbers that better represent the similarity

for uk_url in uk_list:
    #extraction = process.extract(item, us_list, limit=2)

    for us_url in us_list:
        similarity = fuzz.ratio(uk_url, us_url)
        #print(f"UK URL: {item}. US URL: {url}. Similarity: {similarity}")
        result["UK_URL"].append(uk_url)
        result["US_Match_URL"].append(us_url)
        result["Similarity"].append(similarity)
        if similarity == 100:
            us_list.remove(us_url)


data = pandas.DataFrame(result)

#TODO: sort by similarity

#TODO: head should be defined by a user or minimum percentage similarity - but this will also depend on the additional
#functions, such as analysing titles and h1s

sorted_data = data.sort_values(['UK_URL', 'Similarity'],ascending=False).groupby('UK_URL').head(5)

sorted_data.to_csv("Result.csv")

#TODO: add domain names back

#TODO: remove all if 100 exists

#TODO: leave top 10 if no 100% match found - ask the user how many they want to leave

#TODO: add a function if a user wants to see all variants even if a total match is available