import re
url = input("URL: ")
if matches := re.search(r"^(?:https?)?(?:www\.)?twitter\.com/([\w]+)$", url, re.IGNORECASE):
    print("Username: ", matches.group(1))