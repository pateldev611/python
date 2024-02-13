# def greet(name,time):
#     print(f'Good {time} {name},hope you are well')
# name=input('enter ur name:') 
# time=input('enter the time of day:')

# greet(name,time)
   

def area(radius):
    return 3.124*radius*radius

def vol(area,length):
    print(area*length)
radius=int(input('enter a radius')) 
length=int(input('enter the length:'))

area_calc=area(radius)
vol(area_calc,length)



