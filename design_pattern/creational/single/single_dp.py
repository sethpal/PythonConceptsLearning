class Singleton:
    __shared_instance = "singleton"

    @staticmethod
    def getInstance():
        if Singleton.__shared_instance == "singleton":
            Singleton()
        return Singleton.__shared_instance

    def __int__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != "singleton":
            raise Exception("This is Singleton")
        else:
            Singleton.__shared_instance = self


