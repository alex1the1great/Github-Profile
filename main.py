import requests
from bs4 import BeautifulSoup as bs


github_user = input('Input github username: ')
github_url = f'https://github.com/{github_user}'

try:
    r = requests.get(github_url)  # request github profile
    soup = bs(r.content, 'html.parser')  # parsing response as html.

    # Get person name, followers, following & stars.
    person_name = soup.find('span', {'itemprop': 'name'}).get_text().strip()
    followers = soup.find('a', {'href': f'/{github_user}?tab=followers'}).span.get_text()
    following = soup.find('a', {'href': f'/{github_user}?tab=following'}).span.get_text()
    stars = soup.find('a', {'href': f'/{github_user}?tab=stars'}).span.get_text()

    profile_info = f"""{person_name}
followers: {followers}, following: {following}, stars: {stars}"""
    print(profile_info)
except TypeError:
    print('Invalid user name.')
