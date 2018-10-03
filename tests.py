import csv
import glob
import os

if __name__ == "__main__":
    names_to_ignore = ['Black.png', 'BurntSienna.png', 'Cobalt.png', 'Crimson.png', 'ForestGreen.png', 'Grey.png', 'Lime.png', 'Orange.png', 'Pink.png', 'Purple.png', 'Saffron.png', 'SkyBlue.png', 'TitaniumWhite.png', 'Platinum.png']

    # test = ['Blue.png', 'Green.png', 'Red.png', 'Yellow.png']
    
    tracked_items = []

    print('## Missing images listed in database')
    print()
    missing_images = 0
    
    with open('rl-item-database.csv', newline='') as database_file:
        database = csv.DictReader(database_file)

        for row in database:
            if not row['FileLocation'] == '':
                if not os.path.exists(os.path.join('Rocket League Item Images', row['FileLocation'])):
                    print(' - [ ]', row['ID'] + ':', row['FullName'], 'is missing from', row['FileLocation'])
                    missing_images += 1
                else:
                    tracked_items.append(row['FileLocation'])

    print()
    print('## Database items without image')
    print()
    no_image = 0

    with open('rl-item-database.csv', newline='') as database_file:
        database = csv.DictReader(database_file)
        
        for row in database:
            if row['FileLocation'] == '':
                print(' - [ ]', row['ID'] + ':', row['FullName'])
                no_image += 1
        

    print()
    print('## Images not in database')
    print()
    not_in_database = 0

    for image in glob.iglob('Rocket League Item Images/**/*.png', recursive=True):
        corrected_image_name = image[len('Rocket League Item Images/'):].replace('\\', '/') 
        if corrected_image_name not in tracked_items and corrected_image_name.split('/')[-1] not in names_to_ignore:
            print(' - [ ]', corrected_image_name)
            not_in_database += 1

    # ignore = []
    #
    # for image in glob.iglob('Rocket League Item Images/**/*.png', recursive=True):
    #     corrected_image_name = image[len('Rocket League Item Images/'):].replace('\\', '/') 
    #     if corrected_image_name.split('/')[-1] not in ignore and corrected_image_name not in tracked_items:
    #         ignore.append(corrected_image_name.split('/')[-1])
    #
    # print(ignore)


    print()
    print('## Quick Stats')
    print()

    print('Missing images listed in database:', missing_images)
    print('Database items without image:\t', no_image)
    print('Images not in database:\t\t', not_in_database)
