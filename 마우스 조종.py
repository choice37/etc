import subprocess
import os
import pyautogui
from pywinauto.application import Application

'''app = Application()
iffview = app.window_(title_re=".*IrfanView")
irfview.DrawOutline()'''
# print(os.getcwd())
#subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
#pyautogui.press('a')
'''
# 메모장를 띄운다.
app = Application().start("notepad.exe")
 
# '도움말' > '메모장 정보' 메뉴를 선택한다.
app.UntitledNotepad.menu_select("도움말(&H)->메모장 정보(&A)")
 
# '확인' 버튼을 눌러서 다이얼로그를 닫는다.
app.메모장_정보.확인.click()
 
# 메모장에 내용을 적는다.
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
'''
# 메모장를 띄운다.
app = Application().start("pika.exe")

app.Main.set_focus()
while True:
    app.Main.type_keys('{ENTER}')
app.Main.type_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
# '도움말' > '메모장 정보' 메뉴를 선택한다.
app.UntitledNotepad.menu_select("도움말(&H)->메모장 정보(&A)")
 
# '확인' 버튼을 눌러서 다이얼로그를 닫는다.
app.메모장_정보.확인.click()
 
# 메모장에 내용을 적는다.
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
