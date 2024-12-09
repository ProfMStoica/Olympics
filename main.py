"""Main module that starts the application"""

from application import Application

try:
    #dependency/USES relationship between main and Application
    app = Application()

    #run the application
    app.run()
except Exception as ex:
    print(f"An unknown error ocurred.\n{ex}")