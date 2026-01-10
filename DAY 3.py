age = 18
height = 166,6
complex_number = 1 + 1j


triangle_base = input('Triangle base: ')
triangle_height = input('Triangle height: ')
triangle_area = 0.5 * (int(triangle_base)) * (int(triangle_height))
print('The area of the triangle is ' , int(triangle_area))


side_a = input('Triangle side a: ')
side_b = input('Triangle side b: ')
side_c = input('Triangle side c: ')
triangle_perimeter = (int(side_a)) + (int(side_b)) + (int(side_c))
print('The perimeter of the triangle is ' , int(triangle_perimeter))


length = input('Input length: ')
width = input('Input width: ')
area = (int(length)) * (int(width))
perimeter = 2 * ((int(length)) + (int(width)))
print('The perimeter is ' , int(perimeter))
print('The area is ' , int(area))



radius = input('Input radius: ')
circle_area = 3.14 * ((int(radius)))**2
circumference = 2 * 3.14 * (int(radius))
print('The area is ' , int(circle_area))
print('The circumference is ' , int(circumference))



#y=mx+b
slope = 2
y_intercept = -2
x_intercept = -(int(y_intercept)) / (int(slope))
print("Slope: ", slope)
print("X-intercept: ", x_intercept)
print("Y-intercept: ", y_intercept)


x1, y1 = 2, 2
x2, y2 = 6, 10
slop = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope:", slop)
print("Distance:", distance)


print("Are slopes equal?", slope == slop)



x = input('x= ')

y = (int(x)**2) + 6 * (int(x)) + 9


print(len('python') != len('dragon'))


print(('on' in 'python') and ('on' in 'dragon'))

print('I hope this course is not full of jargon:', 'jargon' in 'I hope this course is not full of jargon')

print(('on' not in 'dragon') and ('on' not in 'python'))

len_py = len('python')
float_py = float(len_py)
str_py = str(len_py)
print(len_py,float_py,str_py)

print(7 // 3 == int(2.7))

print(type(10) == type("10"))

print(int(float('9.8')) == 10)

hours = input('Input hours: ')
rate_per_hour = input('Input rate per hours: ')
pay = (int(hours)) * (int(rate_per_hour))
print("Pay:", pay)

number_of_years = input("Enter number of years you have lived: ")
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60
seconds = (int(number_of_years)) * days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute
print("You have lived for ", seconds, " seconds.")

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")







