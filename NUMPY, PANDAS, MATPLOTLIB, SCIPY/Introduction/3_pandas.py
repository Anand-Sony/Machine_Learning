import pandas as pd

data = {"cars" : ["BMW" , "Volvo" , "Ford"] ,
        "bike" : ["Suzuki" , "KTM" , "Royal Enfield"]
        }
data = pd.DataFrame(data)
print(data)

'''
    cars           bike
0    BMW         Suzuki
1  Volvo            KTM
2   Ford  Royal Enfield
'''
print("")


print("Student Data :- ")
# now lets make a data for the students : 
from numpy import random
studentData = {"name" : ["Joe" , "Joe1" , "joe2"],
               "subjects" : ["Science" , "Maths" , "Hindi"],
               "Marks" : random.randint(100 , size=(3))
               }
studentData = pd.DataFrame(studentData)
print(studentData)
'''
Student Data :- 
   name subjects  Marks
0   Joe  Science     82
1  Joe1    Maths     45
2  joe2    Hindi     56
'''