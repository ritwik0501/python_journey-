# s=" ritwik ghosh "
# print(s.strip())
# print(s.upper())
# print(s.lower())
# print(s.replace("ghosh", "anu"))
# print(s.split())
# s1=s.split();
# print(s1.join())
# print(",".join(s1))

#Drills 
#- [ ] Reverse a string three ways: slicing, a loop, and `"".join(reversed(s))`.
# s="ritwik ghosh"
# [::-1] means [start : stop : step]
#sol 1: print(s[::-1])

# sol 2 :for i  in range(len(s)-1,-1,-1):
#     print(s[i],end="")

# sol 3: 
# print("".join(reversed(s)))    

##drills:2
#  [ ] Given `"  Hello, World!  "`, chain methods to produce `"hello world"`.
# s="  Hello, World!  "
# print(((s.strip()).lower()).removesuffix("!").replace(",",""))

#drills :3
#- [] Format the number `1234.5678` as `$1,234.57` using an f-string.
# :   → formatting starts
# ,   → add thousands separators
# .2  → keep 2 decimal places
# f   → format as a floating-point number
# s='1234.5678'
# print(f"${float(s):,.2f}")


### Exercises
# - [ ] **Palindrome checker:** ignore case, 
# spaces, and punctuation. Test with "A man, a plan, a canal: Panama".

# print("Enter a sentecne to check wheather it is palindrom or not")
# str1=str(input())

# clean_str1=''
# for c in str1:
#     if c.isalnum():
#         clean_str1+=clean_str1


# if clean_str1==clean_str1[::-1]:
#     print("Palindrom")
# else:
#     print("Not palindrom")


#  **Word statistics:** given a paragraph, 
# report word count, character count (with and without spaces), average word length, and longest word.

# print('Enter a para ')
# para=str(input())

# word_count=len(para.split(" "))
# count=0
# count_with_spaces=len(para)
# longest_word=""
# check_longest_word=(para.split())
# for str in check_longest_word:
#     if len(str)>len(longest_word):
#         longest_word=str
# print(longest_word)

# for char in para:
#     if char != " ":
#          count += 1
         
         

# average_word_lenth= count/len((para.split()))
# print(average_word_lenth)


#[ ] **Caesar cipher:** shift each letter by N positions, wrapping Z→A, 
# preserving case and leaving non-letters alone. (`ord()` and `chr()` are your tools.)


# print("Enter a text/string")
# text=str(input())
# print("Enter how much position you want to shift")
# position=int(input())

# result=""

# for char in text:
    
#     if "A"<=char<="Z":
#         number=ord(char) - ord("A")
#         number=(number+position)%26
#         new_char=chr(number+ord("A"))
#         result +=   new_char

#     elif "a" <= char <= "z":
#         number=ord(char)-ord("a")
#         number=(number+position)%26
#         new_char=chr(number + (ord("a")))
#         result+=new_char
#     else:
#         result+=char

# print(result)
        
### Mini-project
# - [ ] **Text Analyzer / Password Strength Checker (150–200 lines):** 
# the user pastes text; you report readability stats, most-repeated words, and vowel/consonant ratio. 
# Second mode checks a password against length, mixed case, digit, and 
# symbol rules, then prints a rated verdict with specific improvement suggestions.
#if password have combination of capital letter and small letter and special character and also number then it is a strong password 
# otherwise not  
entry=0
 
while(entry!=3):
    print("1.Text Analyzer")
    print("2.Password Strength Checker")
    print("3.Exit")
    entry=int(input())
    match entry:
        case 1:
            print("Enter a text to analyze")
            text=str(input())
            print("starting readbility..")
            len_text=len(text)
            char_count=0
            special_char=0
            for char in text:
               if "A" <= char <= "Z" or "a" <= char <="z":
                    char_count += 1
               elif char!=" ": 
                   special_char += 1

            vowel_count=0
            consonant_count=0  
            for char in text:
                if char in "aeiouAEIOU":
                    vowel_count += 1
                elif char!=" ":
                    consonant_count +=1

                if vowel_count > 0:
                    ratio_of_vowel_consonant = consonant_count / vowel_count
                else:
                    ratio_of_vowel_consonant = 0

            print(f"Total characters : {len_text}")
            print(f"Letters          : {char_count}")
            print(f"Special chars    : {special_char}")
            print(f"Vowels           : {vowel_count}")
            print(f"Consonants       : {consonant_count}")
            print(f"Consonant/Vowel ratio: {ratio_of_vowel_consonant:.2f}")

        case 2:
            print("Enter a password to check its strength")
            password=str(input())
            capital,small,special_character,number,length8=0,0,0,0,0
            length_check=len(password)
            if length_check >=8:
                length8=1
            for pas in password:
                if "a"<=pas<= "z":
                    small=1
                elif "A"<=pas<= "Z":
                    capital=1
                elif pas.isdigit():
                    number=1
                 
                else :
                    special_character=1

            values=[capital,small,special_character,number,length8]

            zero_count = values.count(0)
            result = 5 - zero_count

            print(f"Your password is rated {result} out of 5")

        case 3:
            print("Ending....")
            exit()
   
                    





    

