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

        if choice == '1':
            lookup_choice = input("Enter lookup type (1. Art Object, 2. Artist, 3. Exhibition): ")

            if lookup_choice == '1':
                id_no = input("Enter Art Object ID: ")
                sql_command = f"SELECT * FROM ART_OBJECT WHERE Id_no = {id_no}"
                result = execute_sql(connection, sql_command)

                if result:
                    print("Art Object Information:")
                    for row in result:
                        print(row)
                else:
                    print(f"No Art Object found with ID {id_no}")

            elif lookup_choice == '2':
                artist_name = input("Enter Artist Name: ")
                sql_command = f"SELECT * FROM ARTIST WHERE Name LIKE '%{artist_name}%'"
                result = execute_sql(connection, sql_command)

                if result:
                    print("Artist Information:")
                    for row in result:
                        print(row)
                else:
                    print(f"No Artist found with name {artist_name}")

            elif lookup_choice == '3':
                exhibition_name = input("Enter Exhibition Name: ")
                sql_command = f"SELECT * FROM EXHIBITION WHERE Name LIKE '%{exhibition_name}%'"
                result = execute_sql(connection, sql_command)

                if result:
                    print("Exhibition Information:")
                    for row in result:
                        print(row)
                else:
                    print(f"No Exhibition found with name {exhibition_name}")

            else:
                print("Invalid lookup type. Please enter 1, 2, or 3.")
        
        elif choice == '2':
            print()
            print("Insert New Tuple:")
            print("1. Artist")
            print("2. Collection")
            print("3. Exhibition")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                artist_name = input("Enter Artist Name: ")
                date_born = input("Enter Date Born (YYYY-MM-DD): ")
                date_died = input("Enter Date Died (YYYY-MM-DD): ")
                country_of_origin = input("Enter Country of Origin: ")
                epoch = input("Enter Epoch: ")
                main_style = input("Enter Main Style: ")
                description = input("Enter Description: ")

                sql_command = f"INSERT INTO ARTIST (Name, DateBorn, Date_died, Country_of_origin, Epoch, Main_style, Description) " \
                            f"VALUES ('{artist_name}', '{date_born}', '{date_died}', '{country_of_origin}', '{epoch}', '{main_style}', '{description}')"

                result = execute_sql(connection, sql_command)

                if result:
                    print("Tuple inserted successfully!")
                else:
                    print("Error inserting tuple.")

            elif choice == '2':
                collection_name = input("Enter Collection Name: ")
                collection_type = input("Enter Collection Type: ")
                collection_descr = input("Enter Collection Description: ")
                Collection_add = input("Enter Collection address: ")
                collection_phone = input("Enter Collection Phone Number (xxx-xxx-xxxx): ")
                collection_contact = input("Enter Collection Contact person: ")

                sql_command = f"INSERT INTO COLLECTION (Name, Type, Description, Address, Phone, Contact_person) " \
                            f"VALUES ('{collection_name}', '{collection_type}', '{collection_descr}', '{Collection_add}', '{collection_phone}', '{collection_contact}')"

                result = execute_sql(connection, sql_command)

                if result:
                    print("Tuple inserted successfully!")
                else:
                    print("Error inserting tuple.")
    

            elif choice == '3':
                exhibit_name = input("Enter Exhibition Name: ")
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date_input = input("Enter End Date (YYYY-MM-DD) or 'NULL' for ongoing: ")
                end_date = f"NULL" if end_date_input.upper() == 'NULL' else f"'{end_date_input}'"

                sql_command = f"INSERT INTO EXHIBITION (Name, Start_date, End_date) " \
                  f"VALUES ('{exhibit_name}', '{start_date}', '{end_date}')"

                result = execute_sql(connection, sql_command)

                if result:
                    print("Tuple inserted successfully!")
                else:
                    print("Error inserting tuple.")
            
        elif choice == '3':
            print()
            print("Update and Delete Tuple:")
            print("1. Update Tuple")
            print("2. Delete Tuple")
            print("3. Back to Main Menu")

            sub_choice = input("Enter your choice (1-3): ")

            if sub_choice == '1':
          
                table_name = input("Enter the table name: ")
                condition_column = input("Enter the reference column: ")
                condition_value = input("Enter the reference column value: ")
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                

                sql_command = f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {condition_column} = '{condition_value}'"
                result = execute_sql(connection, sql_command)

                if result:
                    print("Tuple updated successfully!")
                else:
                    print("Error updating tuple.")

            elif sub_choice == '2':
                
                table_name = input("Enter the table name: ")
                condition_column = input("Enter the condition column: ")
                condition_value = input("Enter the condition value: ")

                sql_command = f"DELETE FROM {table_name} WHERE {condition_column} = '{condition_value}'"
                result = execute_sql(connection, sql_command)

                if result:
                    print("Tuple deleted successfully!")
                else:
                    print("Error deleting tuple.")

            elif sub_choice == '3':
                break  

            else:
                print("Invalid choice. Please enter a number from 1 to 3.")

        elif choice == '4':
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
