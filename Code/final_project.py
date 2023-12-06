import mysql.connector

def get_database_connection():
    user = input("Enter MySQL username: ")
    password = input("Enter MySQL password: ")
    database = input("Enter the name of the database: ")

    connection = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database=database
    )

    return connection

def execute_sql(connection, sql):
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        connection.commit()
        print("Query executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def execute_script(connection, script_path):
    with open(script_path, 'r') as file:
        sql_script = file.read()
        execute_sql(connection, sql_script)

def admin_interface():
    connection = get_database_connection()

    while True:
        print("\nAdmin Interface:")
        print("1. Execute SQL Command")
        print("2. Execute SQL Script")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            sql_command = input("Enter SQL Command: ")
            execute_sql(connection, sql_command)

        elif choice == '2':
            script_path = input("Enter SQL Script Path: ")
            execute_script(connection, script_path)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

    connection.close()

def employee_interface():
    connection = get_database_connection()

    while True:
        print("\nEmployee Interface:")
        print("1. Lookup Information")
        print("2. Insert New Tuple")
        print("3. Update and Delete Tuple")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")

        # Implement the operations for employee_interface

        if choice == '4':
            break

    connection.close()

def guest_interface():
    connection = get_database_connection()

    while True:
        print("\nGuest Interface:")
        print("1. Data Lookup")
        print("2. Quit")
        
        choice = input("Enter your choice (1-2): ")

        # Implement the operations for guest_interface

        if choice == '2':
            break

    connection.close()

if __name__ == "__main__":
    role = input("Enter your role (admin/employee/guest): ")

    if role == 'admin':
        admin_interface()
    elif role == 'employee':
        employee_interface()
    elif role == 'guest':
        guest_interface()
    else:
        print("Invalid role.")
