car_speed = int(input('Enter the car speed: '))

if car_speed <= 80:
    print('this car it is in speed good')
else:
    speed_fine = 7 * (car_speed - 80)
    print(f'the value of fine is R${speed_fine}')
