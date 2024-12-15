import ast
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class AppWindow(Screen):
    pass

class Main(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.screen = FirstWindow()
        return Builder.load_file("Registation.kv")  # Ensure this file exists

    def log_in(self, username, password):
        try:
            with open('daatabase.txt') as f:
                data = f.read()

            # Reconstructing the data as a dictionary
            database = ast.literal_eval(data)

            if username not in database:
                # Update the dictionary with the new username and password
                database[username] = password

                # Write the updated dictionary back to the file
                with open('daatabase.txt', 'w') as data_file:
                    data_file.write(str(database))

                self.root.current = 'AppWindow'  # Switch to AppWindow screen
            else:
                print("User already exists")
        except Exception as e:
            print(f"Error during login: {e}")

    def sign_up(self, username, password):
        try:
            with open('daatabase.txt') as f:
                data = f.read()

            database = ast.literal_eval(data)

            if username in database:
                print("Username already exists!")
            else:
                database[username] = password
                with open('daatabase.txt', 'w') as data_file:
                    data_file.write(str(database))
                self.root.current = 'AppWindow'  # Switch to AppWindow screen
        except Exception as e:
            print(f"Error during sign up: {e}")

if __name__ == '__main__':
    Main().run()
