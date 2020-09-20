from csv import reader

def open_to_list(path_to_file):
    open_file = open(path_to_file, encoding='utf8')
    read_file = reader(open_file)
    return list(read_file)

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row, '\n')

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

apple_store_apps = open_to_list('AppleStore.csv')
google_play_apps = open_to_list('GooglePlayStore.csv')

explore_data(apple_store_apps)
explore_data(google_play_apps)