# We use the psycopg2 library to help us connec to the Postgres SQL database
# This library is already installed on stearns.mathcs.carleton.edu
import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():

    # You will need to change the Password to use this code
    
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
def test_query_one():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="lamm2",
        user="lamm2",
        password="corn453smile")

    cur = conn.cursor()

    sql_population = """DROP TABLE IF EXISTS population;
    CREATE TABLE population
        (code text,
        state text,
        pop int
        ); 
    """
    sql_toponek = """DROP TABLE IF EXISTS toponek;
    CREATE TABLE toponek
    (city text,
    states text, 
    population int, 
    lat real,
    lon real
    );   
"""
    cur.execute( sql_population )
    cur.execute( toponek )

    # fetchone() returns one row that matches your query
    row = cur.fetchone()

    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    #IMPORTANT: This function doesn't actually change the database
    #If we are trying to change the database ...
    # ... for example, creating a table
    #Then we need the following command to finalize our changes

    conn.commit()
    
    return row



# This function sends a query that returns many items
def test_query_all():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mlepinski",
        user="mlepinski",
        password="MyDatabasePassword")

    cur = conn.cursor()

    sql = "SELECT name, abb FROM states"
    
    cur.execute( sql )

    # fetchall() returns a list containing all rows that matches your query
    row_list = cur.fetchall()

    # It is often useful to loop through all rows in a query result
    for row in row_list:
        print( row[1] )
    
    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    # Here I am leaving out the conn.commit() because we aren't changing
    #    either the database or the data in the database
    
    return None


#Often we want to put a Python variable into an SQL query
def test_query_variable():
    
    # You will need to change the Port and the Password to use this code

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mlepinski",
        user="mlepinski",
        password="MyDatabasePassword")

    cur = conn.cursor()


    # Here the %s signals that we will replace this with a variable later
    sql = "SELECT name, abb FROM states WHERE abb = %s OR abb = %s "

    state_abb1 = 'MN'
    state_abb2 = 'NM'
    
    cur.execute( sql, [state_abb1, state_abb2]  )

    # IMPORTANT: We need a list of values for the second input to execute
    #   ... Even if we are only inserting my variable, it must be in a list
    # For example,  [state_abb1]
    
    row_list = cur.fetchall()

    for row in row_list:
        print(row)

    return None

print( test_query_one() )

# test_query_all()

# test_query_variable()


