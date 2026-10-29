from faker import Faker

f = Faker()
for i in range(2):
    print("_______________________")
    pro = f.simple_profile()
    for key in pro:
        print(f"{key} : {pro[key]}")
        



