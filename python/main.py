from pyfiglet import Figlet
import LoginManager

class Session:
    def __init__(self):
        self.user_email = ""
        self.user_password = ""
        self.user_name = ""
        self.logged_in = False

        self.getDetails()
        self.displayWelcome()
        self.main()

    def getDetails(self):
        res = LoginManager.checkLogin()
        if res[0]:
            self.user_email = res[1]
            self.user_password = res[2]
            self.user_name = res[3]
        self.logged_in = res[0]

    def displayWelcome(self):
        if not self.logged_in:
            print(Figlet(font="slant").renderText("Welcome to Arle"))
        else:
            print(Figlet(font="slant").renderText("Arle"))

    def displayHelp(self):
        print("lul")

    def main(self):
        while True:
            command = input(self.user_name + "$ ")
            if command.lower() == "exit":
                print(Figlet().renderText("Cya!"))
                exit(0)
            elif command.lower() == "help" or command.lower() == "panic":
                self.displayHelp()
            elif command.lower() == "login":
                pass
            elif command.lower() == "signup":
                pass
            elif command.split(" ")[0].lower() == "group":
                pass
            elif command.split(" ")[0].lower() == "create": # group, post, comment
                pass
            else:
                pass

if __name__ == "__main__":
    s = Session()
