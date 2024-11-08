def remove_duplicate_lines(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    unique_lines = set(lines)

    with open(path, 'w') as file:
        file.writelines(unique_lines)


if __name__ == '__main__':
    # Specify the path to your text file
    file_path = 'G:/Python/Repositories/GameHubDataBase/src/scraping/top_games_rawg_big_version.txt'
    remove_duplicate_lines(file_path)


