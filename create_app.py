import os

# class definition

class CreateApp():

    def __init__(self, app_name, app_type) -> None:
        self.app_name = app_name
        self.app_type = app_type
        self.app_loc = os.getcwd()

    # Check if the application is already existed
    def check_existence(self):
        self.path = os.path.join(self.app_loc, self.app_name)
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
        os.mkdir(os.path.join(self.path))
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

    def __repr__(self):
        print(f'APP NAME:{self.app_name}, APP_TYPE: {self.app_type}')

# test = CreateApp('test','flask')
# test.check_existence()
# test.app_init()

# test1 = CreateApp('test1', 'front-end')
# test1.check_existence()
# test1.app_init()


# Program logic
while True:
    status = True
    print('Generating project using this script.')
    option = input('Do you want to create new project? y/n \n').lower()
    if option == 'n':
        status = False
    elif option == 'y':
        types = ['front-end', 'flask']
        app_name = input('Enter application name: ')
        print('Select your app types: ')
        print('1. Front End')
        print('2. Flask')
        select = int(input('1 or 2: '))
        if select == 1:
            app = CreateApp(app_name, types[0])
            if app.check_existence() == False:
                app.app_init()
                status = False
            else:
                pass
        elif select == 2:
            app = CreateApp(app_name, types[1])
            if app.check_existence() == False:
                app.app_init()
                status = False
            else:
                pass
        else:
            pass
    else:
        print('Invalid options. Choose again:')
    if status == False:
        break
