import asyncio as asy
import random
from time import time
from time import sleep

async def find_avrg_high(arr,mode): #Функція для видалення елементів які більше або менше середнього значення
    avr = 0
    res = []
    for i in arr: #Знаходимо середнє значення массиву
        avr += i
    avr = avr / len(arr)



    print("AVR = {:.2F}".format(avr))#Виводимо середнє значення.
    await asy.sleep(1)#Визиваєм функцию сліп із бібліотеки asincio. await повідомляє циклу подій
    #що якщо є інші запроси то виконуй їх а ми повідомимо коли цей закінчить роботу
    # sleep(2)

    if mode == True:#в залежності від режиму видаляємо або елементи або більше серед знач або менше
        for i in arr:
            if i > avr:
                res.append(i)
        print("Remove lover avr",res)
    else:#залишаємо елементи менше серед значення
        for i in arr:
            if i < avr:
                res.append(i)
        print("Remove higher avr",res)

    return res

async def work():#асинхронна функція з основним функціоналом
    arr1, arr2, res_arr = [], [], []

    for i in range(40):#заповнюємо масиви рандомними числами
        arr1.append(random.randint(0,100))
        arr2.append(random.randint(0,200))

    print("Start arr1",arr1)
    print("Start arr2",arr2)

    print("\n")

    task1 = asy.create_task(find_avrg_high(arr1,True))#створюємо задачі за допомогою яких можемо запустити декітька
    task2 = asy.create_task(find_avrg_high(arr2,False))#сопрограм разом

    await task1
    await task2

    arr1 = task1.result()#отримуємо результати робрити асинхронних функцій
    arr2 = task2.result()

    arr1.sort()#сортужмо масиви по зростанню
    arr2.sort()

    print("Sorted arr1", arr1)
    print("Sorted arr2", arr2)

    for i in arr1:#Поєднуємо масиви в один якщо елементи є і в обох масивах
        if i in arr2:
            res_arr.append(i * 10)

    print(res_arr)#виводимо результать з'єднання


def main():
    start = time()
    asy.run(work())#запускаємо нашу головну асинхронну функцію
    print("{:.8F}".format(time()-start))


if __name__ == "__main__":
    main()