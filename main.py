class Data:

    def __init__(self, website, emailOrUsername, password):
        self.website = website
        self.emailOrUsername = emailOrUsername
        self.password = password

    def writeData(self):
        file = open('data.txt', 'a')
        file.write("WEBSITE: {} | EMAIL/USERNAME: {} | PASSWORD: {}\n".format(self.website, self.emailOrUsername, self.password))
        print("Data has added successfully!".upper())
        file.close()

    def getData(self):
        file = open('data.txt', 'r')
        f = file.readlines()
        for line in f:
            print(line)

    def deleteData(self, whichLine):
        self.whichLine = whichLine

        file = open('data.txt', 'r')
        lines = file.readlines()

        del lines[int(whichLine)-1]

        updatedFile = open('data.txt', 'w+')
        for line in lines:
            updatedFile.write(line)
        file.close()

        print("Entry has deleted successfully".upper())

    def deleteAll(self, userConfirm):

        if userConfirm == 'yes':
            file = open('data.txt', 'r+')
            file.truncate(0)
            print("Everything has deleted!".upper())
            file.close()
        elif userConfirm == 'no':
            print("Deletion has cancelled!".upper())

user = Data("GitHub", "TestUsername", "TestUserPW")
user.writeData()
user.deleteData(1)
user.deleteAll('yes')