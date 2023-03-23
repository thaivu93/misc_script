import os

# Class Definition
class CreateApp():

    def __init__(self, app_name, app_type) -> None:
        self.app_name = app_name
        self.app_type = app_type
        self.app_loc = os.getcwd()
        self.path = os.path.join(self.app_loc, self.app_name)

    # Check if the application is already existed
    def check_existence(self):
        return os.path.exists(self.path)

    def create_files(self, files):
        try:
            for file in files:
                with open(os.path.join(self.path, file), 'w') as nf:
                    pass
        except OSError as err:
            print(err)

    def create_folders(self, folders):
        for folder in folders:
            try:
                os.makedirs(os.path.join(self.path, folder))
            except OSError as err:
                print(err)

    # Create folders and files as per project type

    def app_init(self):
        types = ['front-end', 'flask']
        if self.check_existence() == False:
            os.mkdir(self.path)
            if self.app_type == types[0]:
                files = ['index.html', 'styles.css', 'script.js']
                self.create_files(files)
            elif self.app_type == types[1]:
                folders = ['static', 'templates', 'images']
                files = ['app.py', 'config.py', 'models.py']
                self.create_folders(folders)
                self.create_files(files)
            else:
                pass
        else:
            pass
    def __repr__(self):
        print(f'APP NAME:{self.app_name}, APP_TYPE: {self.app_type}')

# Program data and loop
types = ['front-end', 'flask']
is_on = True
# Program logic
while is_on:
    print('Generating project using this script.')
    option = input('Do you want to create new project? y/n \n').lower()
    if option == 'n':
        is_on = False
    elif option == 'y':
        app_name = input('Enter application name: ')
        print('Select your app types: ')
        print('1. Front End')
        print('2. Flask')
        select = int(input('1 or 2: '))
        if select == 1:
            app = CreateApp(app_name, types[0])
            app.app_init()
            is_on = False
        elif select == 2:
            app = CreateApp(app_name, types[1])
            app.app_init()
            is_on = False
        else:
            pass
    else:
        print('Invalid options. Choose again:')
    if is_on == False:
        break
