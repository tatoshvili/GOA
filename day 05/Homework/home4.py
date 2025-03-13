numbers = []  # სია, სადაც შევინახავთ რიცხვებს

for i in range(5):
    num = float(input(f"შეიყვანეთ {i+1}-ე რიცხვი: "))  # მომხმარებელს შემოაქვს რიცხვი
    numbers.append(num)  # ვამატებთ სიაში

average = sum(numbers) / len(numbers)  # ვთვლით საშუალოს
print("საშუალო არითმეტიკული არის:", average)