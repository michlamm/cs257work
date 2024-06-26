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
    northfield = "SELECT city FROM toponek WHERE city = 'Northfield'"
    cur.execute( northfield )
    row = cur.fetchone()
    
    if row is None: 
        return "Northfield not available"
      
    else:
        latitude = "SELECT lat, lon FROM toponek WHERE city='Northfield'"
        cur.execute( latitude )
        row1 = cur.fetchone()
        return (row1)
    
    
def largest():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lamm2",
        user="lamm2",
        password="corn453smile")
    cur = conn.cursor()
    largestpop = "SELECT city from toponek where population = (select max(population) from toponek)"
    cur.execute( largestpop )
    row1 = cur.fetchone()
    return (row1)
def mn():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lamm2",
        user="lamm2",
        password="corn453smile")
    cur = conn.cursor()
    smallestmn = "select city from toponek where population = (select min(population) from toponek where state='Minnesota') limit 1;"
    cur.execute( smallestmn )
    row2 = cur.fetchone()
    return (row2)
def lat():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lamm2",
        user="lamm2",
        password="corn453smile")
    cur = conn.cursor()
    lat = "select city from toponek where lat = (select min(lat) from toponek) limit 1"
    lat2 = "select city from toponek where lat = (select max(lat) from toponek) limit 1" 
    lon = "select city from toponek where lon = (select min(lon) from toponek)"
    lon2 = "select city from toponek where lon = (select max(lon) from toponek)"
    cur.execute( lat )
    lat = cur.fetchone()
    cur.execute( lat2)
    lat2 = cur.fetchone()
    cur.execute (lon )
    lon = cur.fetchone()
    cur.execute( lon2)
    lon2 = cur.fetchone()
    
    return lat2, lon2, lat, lon
def sum():
    conn = psycopg2.connect(
            host="localhost",
            port=5432,   
            database="lamm2",
            user="lamm2",
            password="corn453smile")
    cur = conn.cursor()
    state = input("Enter state: ")
    if len(state)>2:
        sum = "select sum(population) from population where state = %s"
        cur.execute(sum, [state])
        row = cur.fetchone()
        if row[0] == None:
             return "Try a different state or check spelling." 
        else:
            return row
    else:  
        sumcode = "select sum(population) from population where code = %s"
        cur.execute(sumcode, [state])
        row1 = cur.fetchone()
        if row1[0] == None:
             return "Try a different abbreviation or check spelling." 
        else:
            return row1
print( Northfield() )
print( largest())
print( mn())
print( lat())
print( sum())
        
