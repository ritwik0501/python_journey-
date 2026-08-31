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

print('Enter a para ')
para=str(input())

word_count=len(para.split(" "))
count=0
count_with_spaces=0
for char in para:
    if char != " ":
         count += 1
         count_with_spaces+=1
    else:
         count_with_spaces+=1

