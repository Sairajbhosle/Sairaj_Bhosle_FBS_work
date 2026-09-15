feet=int(input('Enter distance in feet :'))
inch=int(input('Enter distance in Inches :'))

Final_inch=inch+feet*12
Centimeter=Final_inch*2.54
meter=Final_inch*0.0254
print(f'Converted Meter={meter} and Converted cm={Centimeter}')