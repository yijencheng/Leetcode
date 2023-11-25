import csv 
import json
from this import d 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8-sig') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    
    return jsonArray
  
def parseArray(jsonArray):
    parsed = []
    for i, item in enumerate(jsonArray):
        parsed.append({
            "itemid": int(item['item_id']),
            "shopid": int(item['shop_id']),
            "score": 0.00618,
            "from": "DSCF",
            "info": "justforyou,DD_TW,DSCF"
        })
    return parsed


csvFilePath = "./csv/product-label.csv"
jsonFilePath = "data.json"
def main():
    jsonArray = csv_to_json(csvFilePath, jsonFilePath)
    jsonArray = jsonArray[:200]

    parsed = parseArray(jsonArray)
     
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(parsed, indent=4)
        jsonf.write(jsonString)

main()