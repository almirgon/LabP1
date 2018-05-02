#coding: utf-8
#@Crispiniano 
#Unidade 1: Fahrenheit Celsius

fahrenheit = float(raw_input())

celsius = ((fahrenheit - 32) * 5)/9
kelvin = celsius + 273.15

print 'Fahrenheit: {:.3f} F'.format(fahrenheit)
print 'Celsius: {:.3f} C'.format(celsius)
print 'Kelvin: {:.3f} K'.format(kelvin)
