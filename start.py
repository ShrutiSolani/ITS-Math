# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from .__init__ import create_app
# import mysql.connector
from .database import mydb

app = create_app()


# mydb = mysql.connector.connect(
#     host = "sql6.freesqldatabase.com",
#     user = "sql6449635",
#     database = "sql6449635",
#     password ="EH7dFtDVqR",
#     port = "3306"
# )


if __name__ == "__main__":
    mydb.create_all()
    app.run()