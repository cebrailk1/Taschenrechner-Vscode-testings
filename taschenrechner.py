rechenart=str(input('Welche Rechenart möchtest du benutzen:'))
zahl1=int(input('Gebe die erste Zahl ein mit der du rechnen möchtest:'))
zahl2=int(input('Gebe die zweite Zahl ein mit der du rechnen möchtest:'))
def new_func():
    return ('Kein gültiger Operator')

if rechenart == '+':
    print(f'{zahl1}{rechenart}{zahl2} = {zahl1+zahl2}')
elif rechenart == '+':
    print(f'{zahl1}{rechenart}{zahl2} = {zahl1-zahl2}')
elif rechenart == '-':
    print(f'{zahl1}{rechenart}{zahl2} = {zahl1+zahl2}')
elif rechenart == '*':
    print(f'{zahl1}{rechenart}{zahl2} = {zahl1*zahl2}')
elif rechenart == '/':
    print(f'{zahl1}{rechenart}{zahl2} = {zahl1/zahl2}')
else:
    print:new_func()