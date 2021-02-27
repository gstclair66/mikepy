#Mike St. Clair
#PA3
#2/14/21

def getHawkID():
    return ["mmshkf"]

def compareToFifty(value1,value2):
    if type(value1) == int and type(value2) == int:
        if value1 >= 0 and value2 >= 0:
            avg = (value1 + value2) / 2
            if avg > 50:
                return "Above 50"
            if avg < 50:
                return "Below 50"
            if avg == 50:
                return "Equal to 50"
            else:
                return "Invalid Input"
        else:
            return "Invalid Input"
    elif type(value1) == str or type(value2) == str:
        if str(value1).isdigit() == True and str(value2).isdigit() == True:
            if int(value1) >= 0 and int(value2) >= 0:
                avg = (int(value1) + int(value2)) / 2
                if avg > 50:
                    return "Above 50"
                if avg < 50:
                    return "Below 50"
                if avg == 50:
                    return "Equal to 50"
                else:
                    return "Invalid Input"
            else:
                return "Invalid Input"
        else:
            return "Invalid input"
    else:
        return "Invalid input"
    
def whatAmI(thing):
    if type(thing) == int:
        if thing >= 0:
            return "Non-Negative Integer"
        else:
            return "Unidentified object"
        
    elif type(thing) == str:
        if thing.isdigit() == True:
            return "String with digits"
        elif thing.isalpha() == True:
            return "String with letters"
        else:
            return "Unidentified object"
       
    else:
        return "Unidentified object"
   
def convertUnits(feet):
    if type(feet) == int:
        if feet >= 0:
            return feet * 12
        else:
            return "I do not understand the input"
    elif type(feet) == float:
        return "I do not understand the input"
    elif type(feet) == str:
        if feet.isdigit() == True:
            return int(feet) * 12
        elif feet.isalpha() == True:
            return "Enter digits, not letters"
        else:
            return "I do not understand the input"
    else:
        return "I do not understand the input"
            
        
