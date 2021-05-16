import PySimpleGUI as sg

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Screen:
    __layout = None
    window = None
    event = None
    values = None
    IMC: float
    IMC_status: float

    def __init__(self, initial_layout, title=''):
        self.__layout = initial_layout
        self.window = sg.Window(title, self.__layout)

    def calculate_imc(self, height, weight):
        self.IMC = round(weight/(height**2),2)
        if self.IMC < 18.5:
            self.IMC_status = 'Underweight'
        elif self.IMC < 25:
            self.IMC_status = 'Normal weight'
        elif self.IMC < 30:
            self.IMC_status = 'Overweight'
        elif self.IMC < 35:
            self.IMC_status = 'Obesity level 1'
        elif self.IMC < 40:
            self.IMC_status = 'Obesity level 2'
        else:
            self.IMC_status = 'Obesity level 3 (morbid)'

    def read_event(self):
        must_continue = True
        self.event, self.values = self.window.read()
        # End program if user closes window or
        # presses the OK button
        if self.event == 'calculate':
            if is_number(self.values["height"]) and is_number(self.values["weight"]):
                if float(self.values["height"]) > 0 and float(self.values["weight"]) > 0:
                    self.calculate_imc(float(self.values["height"]),float(self.values["weight"]))
                    self.window.Element('test_result').Update(f'Your IMC (BMI) is {self.IMC}')
                    self.window.Element('test_result2').Update(f'Status: {self.IMC_status}')
                else:
                    sg.popup_ok('You must enter a positive number in both entries!')
                    self.window.Element('test_result').Update('Input number error 0')
                    self.window.Element('test_result2').Update('')
            else:
                sg.popup_ok('You must enter a positive number in both entries!')
                self.window.Element('test_result').Update('Input number error 1')
                self.window.Element('test_result2').Update('')
        
        if self.event == 'exitapp':
            print('Goodbye')
            must_continue = False
            self.window.close()
        if self.event == sg.WIN_CLOSED:
            must_continue = False
        return must_continue


# Define the home Screen layout
# Create the Screen Object
layout_homescreen = [[sg.Text("IMC Calculator",border_width=4, font=('Helvetica', 10))],
    [sg.Text("Height [m]", border_width=4, font=('Helvetica', 15), size=(10, 1)), sg.InputText(size=(15, 1),key='height')],
    [sg.Text("Weight [kg]", border_width=4, font=('Helvetica', 15), size=(10, 1)), sg.InputText(size=(15, 1),key='weight')],
    [sg.Button("Calculate IMC", key='calculate')],
    [sg.Text("", key='test_result', border_width=4, font=('Helvetica', 15), size=(20, 1))],
    [sg.Text("", key='test_result2', border_width=4, font=('Helvetica', 15), size=(20, 1))]]

home = Screen(title="IMC Calculator", initial_layout=layout_homescreen)

def main_loop():
    while home.read_event():
        pass

# Create an event loop
main_loop()


