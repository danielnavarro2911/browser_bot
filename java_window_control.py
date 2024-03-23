from pyjab.jabdriver import JABDriver
import pyautogui

class java:
    def __init__(self):
        #we get the java window name from java_window_name.txt file
        self.window_name=open('java_window_name.txt',mode='r').readline()

    def connect(self):
        #connect java window using WindowsAccessBridge
        #here we create the variable jab that we will use to click and write
        self.jab=JABDriver(self.window_name,bridge_dll=r"C:\Program Files\Java\jre1.8.0_321\bin\WindowsAccessBridge-64.dll")
        self.jab.maximize_window()
        print('Connection established')
    def click(self,element_name,time=10):
        #click on element
        self.jab.wait_until_element_exist(value=element_name,timeout=time)
        self.jab.find_element_by_name(element_name).click()

    def write(self,text,element_name,enter=False,time=10):
        #write the text variable on element.
        #if enter=True, it presses enter using keyboard
        self.jab.wait_until_element_exist(value=element_name,timeout=time)
        self.jab.find_element_by_name(element_name).send_text(text,simulate=True)
        if  enter:
            pyautogui.press('enter')
    def get_text(self,element_name,time=10):
        #method that gets the text from the element
        self.jab.wait_until_element_exist(value=element_name,timeout=time)
        return self.jab.find_element_by_name(element_name).text
    def wait(self,element_name,time=10):
        self.jab.wait_until_element_exist(value=element_name,timeout=time)
        self.jab.wait_until_element_exist()

