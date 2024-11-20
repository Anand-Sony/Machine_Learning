from numpy import random;
x = random.randint(1000);
print(x) # print any number till 1000

y = random.rand()
print(y) #print number till 1, not more than one

z = random.randint(1000 , size=(5))
print(z)  #[157 310 674 504 380]  gives array of any value of given "size"

a = random.randint(10 , size =(3,3))
print(a)    
""" give 2d array of size 3x3   [[8 9 3]
                                [2 3 1]
                                [0 4 1]] 
                                            """

b = random.choice([1,2,5,8,0])
print(b)    # it randomly selects any number from the list [1,2,5,8,0]

c = random.choice([1,4,5,2,1,0] , size=(3,2))
print(c)    # it randomly selects 3 rows and 2 columns from the list