import urllib.request
import re

# Search list (URL optimized)
search_keywords=["BB%20Ki%20vines","Test%20search"]

def getUrlids(search_keyword):
	print("")
	# print("========================")
	print(search_keyword,end =",")
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	for i in range(5):
		# print("https://www.youtube.com/watch?v=" + video_ids[i], end =",")\
		print(video_ids[i], end =",")
	# print("https://www.youtube.com/watch?v=" + video_ids[0])

def searchForAllKeywords():
	for i in search_keywords:
		getUrlids(i)


def main():
    searchForAllKeywords()
    print("")

if __name__ == "__main__":
    main()

# =IMPORTXML(B1,"//a[@id='thumbnail'][1]")[0].href")"
