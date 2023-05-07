import menu,main_module,time

while True:
    menu.menu()
    match int(input("Enter Your selection: ")):
        case 1:
            main_module.ca()
            time.sleep(3)
        case 2:
            main_module.cp()
            time.sleep(3)
        case 3:
            main_module.sa()
            time.sleep(3)
        case 4:
            main_module.sp()
            time.sleep(3)
        case 5:
            main_module.ra()
            time.sleep(3)
        case 6:
            main_module.rp()
            time.sleep(3)
        case 7:
            main_module.ta()
            time.sleep(3)
        case 8:
            main_module.tp()
            time.sleep(3)
        case 9:
            exit()