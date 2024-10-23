#3. perimeeter of a rectangle

width = int(input("Enter the width of rectangle"))
lenght = int(input("Enter the lenght of rectangle"))
perimeter = (2*width) + (2*lenght)
print(perimeter)


#4.circumference of a circle

radius = int(input("Enter the radius of circle"))
circumference = 2 * 3.14 * radius
print(circumference,"inches")

#5. calculate simple interest

principle = int(input("Enter the principle"))
rate = float(input("Enter the rate"))
time = int(input("Enter the time"))
SI = (principle * rate * time)/ 100
print(SI)

#6. total money in piggy bank

fiveCoin = int(input("Enter the number of five coin"))
noteTen = int(input("Eter the number of ten ruppees note"))
twenNOte= int(input("Enter the number of twentey rupees note"))
fifNote = int(input("Enter the number of fifty rupees note"))
total = 5 * fiveCoin + 10 * noteTen + 20 * twenNOte + 50 * fifNote
print(total)
                    
        

