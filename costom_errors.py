#advanced lists
class StupidProofingFailed(Exception):
    pass
class InsultUser(Exception):
    pass
class LogicError(Exception):
    pass
class CustomError(Exception):
    def __init__(self,error_message):
        self.error_message=error_message
        super().__init__(self.error_message)
if __name__ == "__main__" and 1 ==2:
    raise CustomError("you broke it!")
