class House():
    ### Описание Дома"""
    
    def __init__(self,street,number):
        self.street = street
        self.number = number
    ### Свойства Дома"""                           

    def build(self):    
    ### Сторить Дом " 

     print("Дом на улеце" + self.street, "под  номером" + str(self.number) + "построен")
          
House1 = House("Овражная", 31)
House2 = House("Логвиненко", 7)


print(House2.street)