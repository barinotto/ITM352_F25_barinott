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

#b.	Use the opened URL to get the HTML as lines. Decode each line .decode('utf-8') and print out the line only if it has a <title> tag.
    for line in webpage_content.decode('utf-8').splitlines():
        if '<title>' in line:
            print(line)
            break  # Exit after finding the title line