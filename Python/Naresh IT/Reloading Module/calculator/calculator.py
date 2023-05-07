import calcmenu
import calcmodule
import time
while True:
    calcmenu.menu()
    sel = int(input("Enter Your Selection: "))
    match sel:
        case 1:
            calcmodule.addop()
            time.sleep(3)
        case 2:
            calcmodule.subop()
            time.sleep(3)
        case 3:
            calcmodule.mulop()
            time.sleep(3)
        case 4:
            calcmodule.divop()
            time.sleep(3)
        case 5:
            calcmodule.fdivop()
            time.sleep(3)
        case 6:
            calcmodule.moddivop()
            time.sleep(3)
        case 7:
            calcmodule.exop()
            time.sleep(3)
        case 8:
            exit()