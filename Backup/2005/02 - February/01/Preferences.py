class Preferences:

    def __init__(self, filename = "preferences.dat"):
        self.prefDict = {}          # Dictionary to hold the preferences
        self.prefFile = filename    # Name of the file we use

    def getPref(self, name):
        return self.prefDict[name]

    def setPref(self, name, value):
        self.prefDict[name] = value

    def loadPreferences(self):
        """Load all the preference data."""

        # Note it would be much easier to use the "pickle" module to do this,
        #   but then it wouldn't be a standard text file

        lines = []

        try:
            file = open(self.prefFile, "r")
        except IOError:
            return False
        else:
            lines = file.readlines()
            file.close()

        if inputLine == "":
            # EOF, so we issue an error
            print "WARNING: Preference file was empty."
            return True

        # OK, we've got lines, extract the contents

        for l in lines:

            l.strip()                           # Get rid of any extra whitespace
            name, type, value = l.split(",")    # Extract the stuff
            name.strip()                        # Stripd those
            type.strip()
            value.strip()

            if type == "s"          # String
                pass
            elif type == "i"        # Integer
                value = int(value)
            elif type == "f"        # Float
                value = float(value)

            self.prefDict[name] = value         # Put it into the dictionary

        return True     # Things worked

    def savePreferences(self):    
        """Save the preferences to a file."""

        s = "s"
        i = 5
        f = 2.5

        try:
            file = open(self.prefFile, "w")
        except IOError:
            return False
        else:
            for key in self.prefDict.keys()

                value = self.prefDict[key]

                if value.__class__ == s.__class__:
                    type = "s"
                elif value.__class__ == i.__class__:
                    type = "i"
                elif value.__class__ == f.__class__:
                    type = "f"
                else:
                    print "ERROR: Unknown type for key '" + key + "': " + value.__class__
                    continue

                line = key + "," + type + "," + value + "\n"

            # Everything should be written by now
            
            file.close()

            # Now we're done!

            return True