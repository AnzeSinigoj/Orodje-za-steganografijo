import PySimpleGUI as sg
import sys, pyperclip 
from main import encode
from main import decode

sg.theme('DarkAmber') 

def g_encode():
    layout = [ [sg.Text('Datoteka za enkodiranje'), sg.FileBrowse()],[sg.Text('Sporočilo za enkodiranje'), sg.InputText()],[sg.Button('Enkodiraj!'), sg.Stretch(), sg.Button('Izhod')] ]

    okno2Layout = [ [sg.Text("Shrani sliko kot: "), sg.InputText()], [sg.Button("Shrani!")] ]

    okno3Layout = [ [sg.Text("Encoding sucesfull!")], [sg.Button("Exit")] ]

    okno = sg.Window("Enkodiranje", layout)


    while True:
        event, values = okno.read()
        if event == sg.WIN_CLOSED or event == 'Izhod':
            okno.close()
            sys.exit()
        elif event == 'Enkodiraj!':
            okno.close()
            okno2 = sg.Window("Shrani kot", okno2Layout, element_justification='c')
            event2, values2 = okno2.read()
            if event2 == "Shrani!":
                #print(values["Browse"], values[0], values2[0])
                encode(values["Browse"], values[0], values2[0])
                okno2.close()
                okno3 = sg.Window("Konec", okno3Layout, element_justification='c')
                event, values = okno3.read()
                if event == "Izhod":
                    okno3.close()
                    sys.exit()

def g_decode():
    layout = [ [sg.Text("Izberite sliko za dekodiranje"), sg.FileBrowse()],[sg.Button('Dekodiraj!'), sg.Stretch(), sg.Button('Izhod')]]

    okno = sg.Window("Dekodiranje", layout, element_justification='c')

    while True:
        event, values = okno.read()
        if event == sg.WIN_CLOSED or event == 'Izhod':
           break
        elif event == 'Dekodiraj!':
            okno.close()
            decoded = decode(values["Browse"])
            layout2 = [ [sg.Text("Dekodirana vsebina je:")], [sg.Text(decoded)], [sg.Button("Kopiraj"), sg.Button("Izhod")] ]
            okno2 = sg.Window("Konec", layout2, element_justification='c')
            event2, valute2 = okno2.read()
            if event2 == "Kopiraj":
                pyperclip.copy(decoded) 
            elif event2 == "Izhod":
                break
    okno2.close()
    sys.exit() 

def glavnoOkno():
    ly = [ [sg.Text("Orodje za steganografijo.", font=("Impact, 16"))], [sg.Button('Enkodiranje')], [sg.Button('Dekodiranje')], [sg.Button('Izhod', size=(10,9))]]

    okno = sg.Window("Meni", ly, size=(300, 150), element_justification='c')
    while True:
        event2, values2  = okno.read()
        if event2 == sg.WIN_CLOSED or event2 == 'Izhod':
            sys.exit()
        elif event2 == 'Enkodiranje':
            okno.close()
            g_encode()
        elif event2 == 'Dekodiranje':
            okno.close()
            g_decode() 
glavnoOkno()