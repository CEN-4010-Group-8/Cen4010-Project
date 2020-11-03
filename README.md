Planning folder is for documents related to planning the project(UML diagrams, pseudocode, etc.).
Documents folder is for assignment related documents, such as standup worksheets etc.
ProjectCodeBase is for code only.

# How to run this app 
1. Enter the directory path in your command terminal to start up the Virtual Environment
Your local file path -> cd ProjectCodeBase\booksite-20201103T194130Z-001\booksite
2. Bootup your environment with this command line in your terminal
env/Scripts/activate
# Example if the virtual envirmonent is properly up it should look like this
(env) <- this should be in front of your local disk file path.
3. Finally command to run the app in your localhost.
python manage.py runserver
# If you are successful than you have something similar below
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 03, 2020 - 16:28:32
Django version 3.1.3, using settings 'booksite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.