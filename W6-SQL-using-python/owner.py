class Owner():
    def __init__(self, fname: str, lname: str, email: str):
        self.fname = fname
        self.lname = lname
        self.email = email
    def __str__(self):
        return f"{self.fname}, {self.lname}, {self.email}"

