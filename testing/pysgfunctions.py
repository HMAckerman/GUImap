import PySimpleGUI as sg

layout = [[sg.InputText('Default_Name.txt', key='Filename'),
           sg.FileSaveAs('Save As')],
          [sg.Text('')],
          [sg.Button('Save')],
          [sg.Text('', size=(40, 1), key='Status')]]

window = sg.Window('Save with options', layout)

while True:

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Save':
        filename = values['Filename']
        if filename:
            """ Save action here """
            window['Status'].update(value=f'{filename} saved')

window.close()