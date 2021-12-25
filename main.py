import mechanicalsoup 

browser = mechanicalsoup.StatefulBrowser()
# creating browser object
def get_repo(url):
    browser.open(url)
    page = browser.page
    repos = page.find_all('h3')

    base_url = "https://github.com"
    my_repo = []
    for repo in repos:
        sinrepo = repo.find('a')
        reponame = sinrepo.text.replace("\n", "")
        repourl = sinrepo['href']
        my_repo.append({'name': reponame.replace("  ", ""), 'url': base_url + repourl})

    print("My Repositories \n")
    for repo in my_repo:
        print(f"Name: {repo['name']}")
        print(f"Url: {repo['url']}")
        print("")

username = input("Provide your github username : ")
try: 
    url = f"https://github.com/{username}?tab=repositories"
    get_repo(url)
except:
    print("An error occurred. Please check username")