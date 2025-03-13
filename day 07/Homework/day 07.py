#1) AND და OR ოპერატორების ყველა შესაძლო ვარიანტი:
#AND ოპერატორი (ორივე უნდა იყოს True, რომ შედეგი True იყოს)
True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False
#OR ოპერატორი (საკმარისია ერთი იყოს True, რომ შედეგი True იყოს)
True or True   -> True
True or False  -> True
False or True  -> True
False or False -> False
#2) კოდის ანალიზი ტერმინალის გაშვების გარეშე:
True and False or True or True and False
#ნაბიჯ-ნაბიჯ:
(False) or True or (False)  ->  True or True  -> True
შედეგი: True
print(True and False or True or True and False)  # ვამოწმებთ ჩვენს ვარაუდს

#3) მომხმარებლის მიერ შეყვანილი ორი რიცხვის შედარება
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
print(num1 == num2)  # True თუ ტოლია, False თუ არა

#4) ქულის შეფასება
score = int(input("შეიყვანე შენი ქულა (0-100): "))