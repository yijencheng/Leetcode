Source_A.txt
{ "$uid": 111, "age": 32, "gender": "male" }
{ "$uid": 333, "age": 23, "gender": "female" }
{ "$uid": 222, "age": 18, "gender": "unknown" }

Source_B.txt
{ "$uid": 111, "like": "gaming" }
{ "$uid": 222, "like": "movies" }
{ "$uid": 333, "like": "sports", "birthday": "1991-01-02" }
{ "$uid": 444, "like": "programming" }


SAMPLE OUTPUT
Merged.txt
{ "$uid": 111, "age": 32, "gender": "male", "like": "gaming" }
{ "$uid": 222, "age": 18, "gender": "unknown", "like": "movies" }
{ "$uid": 333, "age": 23, "gender": "female", "like": "sports", "birthday": "1991-01-02" }
{ "$uid": 444, "like": "programming" }


=============================================================
input1 = [{ "$uid": 111, "age": 32, "gender": "male" }]
input2 = [
  { "$uid": 111, "like": "gaming" }, 
{ "$uid": 222, "like": "movies" }, 
{ "$uid": 333, "like": "sports", "birthday": "1991-01-02" }, 
{ "$uid": 444, "like": "programming" },
]

"
d = {}
1. loop through each file
2. for each row(user data) #sourceA
		set uid as key #111: {"age":32, "gender":"male"}
		for each field, set value. if exist alrdy, overwrite
  
for key, jsons in map:

  
  
def main(input1, input2):
  d = {}
  inputs = mergeInput(input1, input2)
  for record in inputs: # O(# of records )
    uid = getUID(record) #O(1)
    cur_user = d.get(uid, {})
    for key, value in record.items(): #O(1)
		  # build new field in temp obj -> get userid -> merge to object
      cur_user[key] = value

    d[uid] = cur_user
  
  res = []
  for uid, jsonValue in d.items():
    # userObject = builduserObject(uid, jsonValue)
    arr.append(jsonValue)

    
def builduserObject(uid, jsonField):
  	# userObj = {
  	# "$uid": uid
  	# }
    jsonField["$uid"] = uid
    # for key, values in jsonField.values():
    #   userObj[key] = value
    return jsonField
    
    
#111: {"age":32, "gender":"male"}