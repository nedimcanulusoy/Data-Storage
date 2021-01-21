class Data:

    def writeData(self, website, emailOrUsername, password):
        self.website = website
        self.emailOrUsername = emailOrUsername
        self.password = password

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

        print("Entry has deleted successfully".upper())

user = Data()
user.writeData("GitHub", "TestUsername", "TestUserPW")
user.deleteData(1)

