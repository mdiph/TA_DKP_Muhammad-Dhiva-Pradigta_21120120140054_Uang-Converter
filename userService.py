class userService(object):
    def __init__(self, email):
        self.email = email
        self.data = [
            "dhiva@gmail.com", "user1@gmail.com","1"
        ]

    def login(self):
        return self.checkCredentials()

    def checkCredentials(self):
        if self.email in self.data:
            return True
        else:
            return False
