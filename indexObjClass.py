class indexObj:

    def __init__(self, start, motherString):
        self.start = start;
        self.end = len(motherString);
        self.motherString = motherString;
    
    
    def __str__(self):
        string = str(self.motherString[self.start:])
        return string

      