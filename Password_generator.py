class Generator():
    def __init__(self,website):
        """This holds the website name and self.vowels"""
        self.website=website#name of the website
        self.vowels=['a','e','i','o','u']#holds all the vowels
        self.number_to_letter=self.letters_to_numbers()
        self.nums_to_symbols=self.num_to_symbol()
        
    def letters_to_numbers(self):
        """This function returns a dictionary with numbers mapping to letters. Num equals the shift"""  
        letters='abcdefghijklmnopqrstuvwxyz'#used for creating the letters to numbers
        l_to_n={}
        count=1
        for l in letters:
            l_to_n[count]=l
            count+=1

        return l_to_n
    
    def num_to_symbol(self):
        """Returns a dictionary that maps numbers to there corresponding keyboard symbol"""
        symbols='!@#$%^&*()'
        num_to_symbol={} 
        count=1
        for c in symbols:
            if count>=10:
                count-=10
            num_to_symbol[count]=c
            count+=1
        return num_to_symbol

    def cesar_cipher(self,shift):
        """returns a dict that maps original characters to their encoded characters based on a shift"""
        cipher={}
        for num,char in zip(self.number_to_letter.keys(),self.number_to_letter.values()):
            if num+shift>26:
                while num+shift>26:
                    num-=26
                cipher[char]=self.number_to_letter[num+shift]
            else:
                cipher[char]=self.number_to_letter[num+shift]
        return cipher
    
    def convert_to_cipher(self,word,shift):
        """This method shifts all the characters of a string then returns it"""
        dictionary=self.cesar_cipher(shift)
        new_word=''
        for w in word:
            try:
                new_word+=dictionary[w]
            except:
                new_word+=w
                continue
        return new_word
    
    def solve(self):
        """This returns a new password based on my algorithm along with the steps"""
        new_password=''#declare the new password
        steps=[]
        steps.append(self.website)
        if len(self.website)%2==0:
            new=[char for char in self.website if char in self.vowels]
            for r in new:
                new_password+=r
            steps.append(new_password)
            new_password=self.convert_to_cipher(new_password, len(self.website))
            steps.append(new_password)
            if len(new_password)<=2:
                new_password+='bee'
                steps.append(new_password)
            new_password=new_password[0].upper()+new_password[1:-1]+new_password[-1].upper()#step 3
            steps.append(new_password)
            n=len(new)*len(new_password)
            new_password+=str(n)
            steps.append(new_password)
        else:
            new=[char for char in self.website if char not in self.vowels]
            for r in new:
                new_password+=r
            steps.append(new_password)
            new_password=self.convert_to_cipher(new_password, len(self.website))
            steps.append(new_password)
            new_password=new_password[0].upper()+new_password[1:-1]+new_password[-1].upper()#step 3
            steps.append(new_password)
            n=len([char for char in self.website if char in self.vowels])*len(new_password)
            
            new_password+=str(n)
            steps.append(new_password)
            
        """Code up here is steps 1,2,3"""
        number=int(str(n)[0]) 
        number=number**2
        
        
        
        if number>9:
            number=round(number/10)
        
        new_password+=self.nums_to_symbols[number]
        steps.append(new_password)
 

        new_password=new_password[::-1]
        steps.append(new_password)
        
        while len(new_password)<8:
            new=self.convert_to_cipher(new_password,len(new_password))
            new_password+=new
            if len(new_password)>=8:
                steps.append(new_password)
                new_password=new_password[::-1]
                steps.append(new_password)
                break
        while len(new_password)>16:
            new_password=new_password[:-1]
            if len(new_password)<=16:
                steps.append(new_password)
                new_password=new_password[::-1]
                steps.append(new_password)
                break
        return new_password,steps
    
    def checks(self,password):
        """This function will check if the password meets all the constraints of a modern password"""
        has_number=False
        has_cap_letter=False
        char_length=False
        special_character=False
        for i in password:
            try:
                i=int(i)
                has_number=True
            except:
                pass            
            if isinstance(i, str):
                if i.isupper():
                    has_cap_letter=True
        
        if len(password)>7 and len(password)<17:
            char_length=True
            
            
        for x in self.nums_to_symbols.values():
            if x in password:
                special_character=True
                
        return has_number,has_cap_letter,char_length,special_character

print('Dont enter the website without www.,https://, or a domain name: ')
website=input("Enter the website: ")
steps_on=input("Do you want to see the steps?(y/n)")

p=Generator(website)

if steps_on=='y':
    for i in p.solve()[1]:
        print(i)
    print('')
    print(p.checks(p.solve()[0]))
else:
    print(p.solve()[0])
    print(p.checks(p.solve()[0]))
