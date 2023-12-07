import mysql.connector
from datetime import datetime

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

def execute_sql(connection, sql, data=None):
    cursor = connection.cursor()

    try:
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)

        if cursor.description:  
            result = cursor.fetchall()
            return result
        else:
            connection.commit()
            return True

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

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
        print("1. Browse Art Objects")
        print("2. Browse Artists")
        print("3. Browse Collections")
        print("4. Browse Exhibitions")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            while True:
                id_no = input("Enter the Art Object ID number: ")

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM ART_OBJECT WHERE Id_no = {id_no}")

                        result = cursor.fetchall()

                        if result:
                            print("\nArt Objects:")
                            columns = [col[0] for col in cursor.description]
                            for i, col in enumerate(columns):
                                print(col, end="\t")  
                            print() 

                            for row in result:
                                print(row)
                            
                            cursor.execute(f"SELECT * FROM PAINTING WHERE Id_no = {id_no}")
                            result_painting = cursor.fetchall()

                            cursor.execute(f"SELECT * FROM SCULPTURE WHERE Id_no = {id_no}")
                            result_sculpture = cursor.fetchall()

                            cursor.execute(f"SELECT * FROM OTHER WHERE Id_no = {id_no}")
                            result_other = cursor.fetchall()

                            if result_painting:
                                print("\nPainting:")
                                columns_painting = [col[0] for col in cursor.description]
                                for i, col in enumerate(columns_painting):
                                    print(col, end="\t")  
                                print()
                                for row in result_painting:
                                    print(row)
                            elif result_sculpture:
                                print("\nSculpture/Statue:")
                                columns_sculpture = [col[0] for col in cursor.description]
                                for i, col in enumerate(columns_sculpture):
                                    print(col, end="\t")  
                                print()
                                for row in result_sculpture:
                                    print(row)
                            elif result_other:
                                print("\nOther:")
                                columns_other = [col[0] for col in cursor.description]
                                for i, col in enumerate(columns_other):
                                    print(col, end="\t")  
                                print()
                                for row in result_other:
                                    print(row)
                            break

                        else:
                            print(f"No art object found with Id_no {id_no}")

                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "2":
            while True:
                name1 = input("Enter the name of the Artist: ")

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM ARTIST WHERE Name LIKE '%{name1}%'")

                        result = cursor.fetchall()

                        if result:
                            print("\nArtists:")
                            columns = [col[0] for col in cursor.description]
                            for i, col in enumerate(columns):
                                print(col, end="\t")  
                            print() 

                            for row in result:
                                print(row)
                            break
                        else:
                            print(f"No Artist found with name {name1}")

                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "3":
            while True:
                name2 = input('Enter the name of the Collection: ')

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM COLLECTION WHERE Name LIKE '%{name2}%'")

                        result = cursor.fetchall()

                        if result:
                            print("\nCollection:")
                            columns = [col[0] for col in cursor.description]
                            for i, col in enumerate(columns):
                                print(col, end="\t")  
                            print() 

                            for row in result:
                                print(row)
                            break
                        else:
                            print(f"No Collection found with name {name2}")

                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "4":
            while True:
                exhibit = input("Enter the name of the Exhibition: ")

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(f"SELECT * FROM EXHIBITION WHERE Name LIKE '%{exhibit}%'")

                        result = cursor.fetchall()

                        if result:
                            print("\nExhibition:")
                            columns = [col[0] for col in cursor.description]
                            for i, col in enumerate(columns):
                                print(col, end="\t")  
                            print() 

                            for row in result:
                                print(row)
                            break
                        else:
                            print(f"No Exhibition found with name {exhibit}")

                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

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
