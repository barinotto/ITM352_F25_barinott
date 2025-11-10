# Ben Barinotto
# 11-06-2025

#assign url to a variable
chicago_page_url = 'https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data'

#import urllib.request
import urllib.request
#import ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#open the url with urlib.request.urlopen() and print out the response
with urllib.request.urlopen(chicago_page_url) as response:
    webpage_content = response.read()
    #print(type(webpage_content))
    #print webpage content and print only the first 500 characters
    print(webpage_content.decode('utf-8')[:500])

    # what is webpage_content and how do you work with it?