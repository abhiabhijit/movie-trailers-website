import urllib.request
import urllib.parse
import re
def search(movie):
  query_string = urllib.parse.urlencode({"search_query" : movie})
  html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
  search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
  link = search_results[0]
  return link
#print(link)

