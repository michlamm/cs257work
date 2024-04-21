# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2    
# This function tests to make sure that you can connect to the database
def test_connection():

    conn = psycopg2.connect(
            host="localhost",
            port=5432,   
            database="lamm2",
            user="lamm2",
            password="corn453smile")
    if conn is not None:
            print( "Connection Worked!" )
    else:
            print( "Problem with Connection" )

    return None


# This function sends an SQL query to the database
def Northfield(): #Determine if Northfield is present in the database. 
                #If it is, print its location (Latitude and Longitude). 
                #If it is not, print an appropriate message for the user.
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lamm2",
        user="lamm2",
        password="corn453smile")
    cur = conn.cursor()

   # sql = "SELECT city FROM table WHERE city = 'Northfield'"
    northfield = "SELECT city FROM toponek WHERE city='Northfield'"

    cur.execute( northfield )
    if data is None: 
        print ("Northfield not available")
    else:
        latitude = "SELECT lat, lon FROM toponek WHERE city='Northfield'"
    # fetchone() returns one row that matches your query
    row = cur.fetchone()
    return (row)

print( Northfield() )
