class RequirementsNotPassed(Exception):
    def __init__(self):
        raise Exception("Requirements Not Passed")
