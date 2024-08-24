import sqlite3


# Create database
def init_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS QUIZ (fullname TEXT, color TEXT, animal TEXT, hobbies TEXT, score INTEGER)""")

    connection.commit()
    connection.close()


# Connect to the database
def connect_db(db_name="quiz.db"):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


# Insert info and quiz records
def insert_records(fullname, color, animal, hobbies, score):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO QUIZ(fullname, color, animal, hobbies, score) VALUES (?,?,?,?,?)",
                   (fullname, color, animal, hobbies, score))
    connection.commit()
    connection.close()


# Get all info
def get_all_info():
    # Connect to the database
    connection, cursor = connect_db()

    # Execute the query to fetch all records
    results = cursor.execute("SELECT * FROM QUIZ").fetchall()

    # Close the connection
    connection.close()
    return results


# Get record by fullname
def get_record_by_fullname(fullname):
    # Connect to the database
    connection, cursor = connect_db()

    # Execute the query to get record of a fullname
    record = cursor.execute(
        "SELECT * FROM QUIZ where fullname=?", (fullname,)).fetchone()

    # Close the connection
    connection.close()
    return record


# Get the best score of a user from database
def get_best_score(fullname):
    connection, cursor = connect_db()
    score = cursor.execute(
        "SELECT score FROM QUIZ WHERE fullname=?", (fullname,)).fetchone()[0]
    connection.close()
    return score


# Update a user's score
def update_score(fullname, score):
    connection, cursor = connect_db()
    cursor.execute(
        "UPDATE QUIZ SET score = ? WHERE fullname = ?", (score, fullname))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    try:
        init_db("quiz.db")
    except:
        print("Database already exists.")
