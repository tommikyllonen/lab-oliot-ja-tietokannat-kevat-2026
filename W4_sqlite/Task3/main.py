from db_conn import DB_CONN 
class Main:
    def __init__(self)-> None:
        print("Program starting.")
        DB_CONN.close()
        print("Program ending.")

        return None


if __name__ == "__main__":
    Main()

