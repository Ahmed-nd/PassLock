# Password validation in Python
# using naive method
  
# Function to validate the password
def password_check(passwd):
    
    SpecialSym=''' [@_!#$%^&*()<>?/\|}{~:];' ",.+- '''
   
    val = True , 0
      
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False , 1
          
    if len(passwd) > 100:
        print('length should be not be greater than 100')
        val = False , 2
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False , 3
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False , 4
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False , 5
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False , 6
    if val:
        return val
    return val
  
