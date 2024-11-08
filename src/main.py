def RawgScraper1():
    import requests
    from bs4 import BeautifulSoup

    response = requests.get("https://rawg.io/?filters=%7B%22ordering%22%3A%5B%22-added%22%5D%7D")
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', class_='game-card-medium__info__name')

    with open('top_games_rawg_big_version.txt', 'a') as f:
        for link in links:
            game_link = link.get("href")
            print(game_link)
            f.write(game_link + '\n')


if __name__ == '__main__':
    RawgScraper1()
