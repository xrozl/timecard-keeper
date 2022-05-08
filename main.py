import PySimpleGUI as sg
import asyncio
import time

sg.theme('Reddit')
layout: list = [
    [sg.Text('Working Time: '), sg.Text('', key='_WORKING_TIME_')],
    [sg.Text('Break Time: '), sg.Text('', key='_BREAK_TIME_')],
    [sg.Text('Total Time: '), sg.Text('', key='_TOTAL_TIME_')],
    [sg.Text('Remaining Time: '), sg.Text('', key='_REMAINING_TIME_')],
    [sg.Text('Status: '), sg.Text('', key='_STATUS_')],
    [sg.Button('start'), sg.Button('rest'), sg.Button('stop')],
    [sg.Column([[sg.Button('exit')]], justification='r')]
]

window: sg.Window = sg.Window('Working Time', layout, resizable=False, size=(220, 190))
window.Finalize()

remain: int = 60*60*8
working: int = 0
break_: int = 0
status: str = 'stop'

async def update_time():
    global remain
    global working
    global break_
    global status
    global layout
    while True:
        if status == 'stop':
            remain = 60*60*8
            working = 0
            break_ = 0
            status = 'stop'
            window['_WORKING_TIME_'].update(str(working))
            window['_BREAK_TIME_'].update(str(break_))
            window['_TOTAL_TIME_'].update(str(working+break_))
            window['_REMAINING_TIME_'].update(str(remain))
            window['_STATUS_'].update('stop')
        elif status == 'work':
            working += 1
            remain -= 1
            layout[4][1].update(str(working))
            window['_WORKING_TIME_'].update(str(working))
            window['_TOTAL_TIME_'].update(str(working+break_))
            window['_REMAINING_TIME_'].update(str(remain))
        elif status == 'rest':
            break_ += 1
            remain -= 1
            layout[4][1].update(str(working))
            window['_BREAK_TIME_'].update(str(break_))
            window['_TOTAL_TIME_'].update(str(working+break_))
            window['_REMAINING_TIME_'].update(str(remain))
        time.sleep(1)
        window.refresh()
        print(remain)

# run
asyncio.run(update_time())

while True:
    event, values = window.read()
    if event == 'exit' or event == sg.WIN_CLOSED:
        break
    elif event == 'start':
        status = 'work'
        pass
    elif event == 'stop':
        status = 'stop'
        pass
    elif event == 'rest':
        status = 'rest'
        pass
window.close()
