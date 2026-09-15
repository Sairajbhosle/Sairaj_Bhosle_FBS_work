rs=4500

twoth=rs//2000
remmon=rs%2000

fivehundn=remmon//500
remmon1=remmon%500

twohun=remmon1//200
remmon2=remmon1%200

hun=remmon2//100
remmon3=remmon2%100

fif=remmon3//50
remmon4=remmon3%50

tw=remmon4//20
remmon5=remmon4%20

tn=remmon5//10
remmon6=remmon5%10

f=remmon6//5
remmon7=remmon%5

totaln=twoth+fivehundn+twohun+hun+fif+tw+tn+f
print(totaln)