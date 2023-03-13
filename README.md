# Database-Managing-Web-App
A Web Application with the purpose to manage the database of a students' volunteering league. The Back-End was done in Flask, Python and the Front-End was created using HTML and vanilla CSS.

Use the script_creare.dll file to create the tables of the database and the relationships between the tables. 

User the script_populare.sql file to populate the tables of the databes.

To run the app, simply run the index.py file in a terminal using the command "python3 index.py". The app should be visible in a browser at the address http://localhost:5000.

!!! IMPORTANT !!! For the app to be runnable, you will have to change the credentials for the database connection on the 14th line in index.py.

If the app returns an error like „An attempt was made to access a socket in a way forbidden by its access permissions”, change the port number at line 6 in the code. Than the app will be visible at the address http://localhost:[port-number].
