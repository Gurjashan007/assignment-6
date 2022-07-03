#Q9
class sol:
    def validity(self,str1):
        accum=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                accum.append(i)
            elif len(accum)==0 or parentheses[accum.pop()]!=i:
                return False
        return len(accum)==0
print(sol().validity("((("))
 
@@ -0,0 +1,38 @@
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:\Users\adity\OneDrive\Desktop\Assignment 6.py ===========
28
(True, True)
NITIN
Yes
      1 

     1 1 

    1 2 1 

   1 3 3 1 

  1 4 6 4 1 

zaqwsxcderfvbgtyhnmjuiklop
True
red-pink-green-black-blue
black-blue-green-pink-red
Student ID: SV12
Student name : Jean Garner
Student class : V
Student ID: SV12
Student name : Jean Garner
To check whether they are instances of said classes or not:
True
False
True
False

To check whether the said classes are subclasses of the built-in object class or not:
True
True
[[-10, 2, 8], [-7, -3, 10]]
False