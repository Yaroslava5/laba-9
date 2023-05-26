def p1():
    from PIL import Image, ImageFilter
    import os

    a = "1.jpg"
    b = "2.jpg"
    c = "3.jpg"
    d = "4.jpg"
    e = "5.jpg"

    h = [a, b, c, d, e]
    count = 0
    for file in h:
        count += 1
        img = Image.open(file)
        new_img = img.filter(ImageFilter.EMBOSS)
        new_img.show()
        try:
            os.mkdir("E:/9_лаба")
        except:
            pass
        new_img.save(f"E:/9_лаба/new_img{count}.png")

def p2():
    from PIL import Image, ImageFilter
    import os

    a = "1.jpg"
    b = "2.tiff"
    c = "3.jpg"
    d = "4.jpg"
    e = "5.jpg"

    h = [a, b, c, d, e]
    count = 0
    for file in h:
        if file.endswith('.jpg') or file.endswith('.png'):
            count += 1
            img = Image.open(file)
            newimg = img.filter(ImageFilter.EMBOSS)
            newimg.show()
            try:
                os.mkdir("E:/9_лаба")
            except:
                pass
            newimg.save(f"E:/9_лаба/newimg{count}.png")

def p3():
    import csv
    file = open("data.csv", "r")
    data = list(csv.reader(file, delimiter=","))
    print("Нужно купить: ")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
    print(f"Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")

p3()