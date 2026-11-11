import json

with open("json-practice/student.json", "r") as file:
    student = json.load(file)

print(student)
student["age"]= 19
student["skills"].append("SQL")
with open("json-practice/student.json", "w") as file:
       json.dump(student,file,indent=1)

print("updated successfully !")