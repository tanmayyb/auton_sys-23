import json
#JSON Program
#Requirements:
#Saver (Edits and saves JSON File)
#Loader (Sends JSON to GUI)

fileName = "sample.json"
parameters = {}



#Edit JSON - Updated parameters is meant to be a dictionary with the new json values
def editJson(updatedParameters):
    #Save JSON File
    def saveJson(newFile, index):
        jsonObject = json.dumps(newFile, indent = index, sort_keys=True)

        with open(fileName, "w") as outfile:
            outfile.write(jsonObject)
        
        print(jsonObject)
        return jsonObject

    # Opening JSON file
    with open(fileName, 'r') as openfile:
    # Reading from json file (produces Python dictionary)
        jsonFile = json.load(openfile)


    for parameter in updatedParameters:
        jsonFile[parameter] = updatedParameters[parameter]
    
    jsonObject = saveJson(jsonFile, len(jsonFile))
    return jsonObject


#Gets values asked from jsonFile and return dictionary of the values as integers (takes in list of keys/values wanted)
def loadJson_param(valuesNeeded):
    #Open file
    with open(fileName, 'r') as openfile:
        jsonFile = json.load(openfile)
    
    #Initialize values 
    values = {}
    #Create dictionary of values needed
    for key in valuesNeeded:
        if key in jsonFile:
            values[key] = int(jsonFile[key])
        else:
            print("Value does not exist.")
    return values

#loads the entire json file 
def loadJson_file():
    #Opens and load file
    with open(fileName, 'r') as openfile:
        jsonFile = json.load(openfile)
    return jsonFile

