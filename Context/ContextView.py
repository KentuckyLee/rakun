class Authantication:
    __instance = None
    _user = None

    @staticmethod
    def getInstance():
        print('...............Context/ContextView/Authantication get_instance function called')
        if Authantication.__instance == None:
            Authantication()
        return Authantication.__instance

    def setUser(self, user):
        u = Authantication.getInstance()
        u._user = user

    def getUser(self):
        u = Authantication.getInstance()
        return u._user

    def __init__(self):
        if Authantication.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Authantication.__instance = self

    def logutInstance(self):
        Authantication.__instance = None
        Authantication._user = None