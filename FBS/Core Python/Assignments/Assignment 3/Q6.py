#Profit or loss
costp=int(input('Enter Cost Price :'))
sellingp=int(input('Enter selling Price :'))
if(costp>sellingp):
    loss=costp-sellingp
    print(f'Loss of rs :{loss}')
else:
    profit=sellingp-costp

    print(f'Profit of rs :{profit}')
