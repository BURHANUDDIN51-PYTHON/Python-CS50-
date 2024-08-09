class Vault:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        
    
potter = Vault(100,25,45)
print(potter)
weasley = Vault(25,15,125)
print(weasley)
total = potter + weasley
print(total)