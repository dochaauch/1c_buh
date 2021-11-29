# Import pywinauto Application class
from pywinauto.application import Application
# Connect to already running process:
app = Application().connect(best_match='1С:Бухгалтерия для Windows 95 - Metsa 10 2011 eur')
#app = Application(backend="uia").connect(title_re=r'.*1С:Бухгалтерия для Windows 95*')
main_dlg = app.window()
#main_dlg.print_control_identifiers()
print_menu = main_dlg.menu_select('Сервис->Принтер...')
print_dlg = app['Настройка печати']
portrait_orient = print_dlg['&КнижнаяRadioButton'].click()
print_dlg.Button2.click()
#app['Настройка печати'].print_control_identifiers()

#print(main_dlg)
