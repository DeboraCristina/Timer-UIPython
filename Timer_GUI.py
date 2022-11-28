import PySimpleGUI as pg
from Timer import *
from icon import *

#variavei
tempo_padrao = {'hora':'00', 'min':'00', 'seg':'00'}
tempo = {'hora':'00', 'min':'00', 'seg':'00'}
pause = False

ICON = icon()
pg.theme('DarkBrown4')
font_texto = ('Arial', 18, 'bold')
font_botao = ('Arial', 10, 'bold')

def definir_tempo():
    global tempo_padrao, tempo, pause
    h, m, s = 0, 0, 0

    # Layout
    hora =    [
        [pg.Button('+', key='h+', pad=0, size=(1, 1)),],
        [pg.Text(text = str(set_num(tempo_padrao['hora'])), font = font_texto, key = 'hora', pad=(None, 15))],
        [pg.Button('-', key='h-', pad=0, size=(1, 1)),]
    ]
    minuto =  [
        [pg.Button('+', key='m+', pad=0, size=(1, 1)),],
        [pg.Text(text = str(set_num(tempo_padrao['min'])), font = font_texto, key = 'minuto', pad=(None, 15))],
        [pg.Button('-', key='m-', pad=0, size=(1, 1)),]
    ]
    segundo = [
        [pg.Button('+', key='s+', pad=0, size=(1, 1))],
        [pg.Text(text = str(set_num(tempo_padrao['seg'])), font = font_texto, key = 'segundo', pad=(None, 15))],
        [pg.Button('-', key='s-', pad=0, size=(1, 1))]
    ]
    coluna = [
        [pg.Column(hora, element_justification='c', pad=0),
         pg.Column(minuto, element_justification='c', pad=0),
         pg.Column(segundo, element_justification='c', pad=0)],
        [pg.Button('Definir', key='definir', pad=(0, (15, 0)))]
    ]
    layout = [
        [pg.Column(coluna, element_justification='c', pad=10)]
    ]
    # Window
    win = pg.Window('Definir Tempo', layout, return_keyboard_events=True, icon=ICON)
    # Loop Principal
    while True:
        event, value = win.read()
        if event == 'h+':
            h = h + 1
        if event == 'h-' and h > 0:
            h = h - 1
        if event == 'm+':
            m = m + 1
        if event == 'm-' and m > 0:
            m = m - 1
        if event == 's+':
            s = s + 1
        if event == 's-' and s > 0:
            s = s - 1
        if event == pg.WINDOW_CLOSED or event == 'Escape:9':
            retorno = False
            break
        if event == 'definir' or event == 'Return:36':
            retorno = True
            tempo_padrao = {'hora':set_num(h), 'min':set_num(m), 'seg':set_num(s)}
            break
        win['hora'].update(set_num(h))
        win['minuto'].update(set_num(m))
        win['segundo'].update(set_num(s))
    win.close()
    return retorno
    pass

def janela_principal():
    global tempo_padrao, tempo, pause
    zerado = False
    # Layout
    coluna = [
        [pg.Button('00:00:00', key='setar_tempo', font = font_botao)],
        [pg.Text(text = '00:00:00', font = font_texto, key = 'tempo', pad=(None, 15))],
        [pg.Button('Iniciar', key='iniciar', pad=(0), font = font_botao),
         pg.Button('Pausar', key='pausar', pad=(0), font = font_botao),
         pg.Button('Resetar', key='resetar', pad=(0), font = font_botao)]
    ]
    layout = [
        [pg.Column(coluna, element_justification='c')]
    ]
    # Window
    win = pg.Window('Title', layout, return_keyboard_events=True, icon=ICON, titlebar_icon=ICON)
    # Loop Principal
    t = 0
    while True:
        event, value = win.read(timeout=500)
        text= win['tempo']
        win['setar_tempo'].update(f'{tempo_padrao["hora"]}:{tempo_padrao["min"]}:{tempo_padrao["seg"]}')

        if event == pg.WINDOW_CLOSED or event == 'Escape:9':
            break

        if event == 'setar_tempo':
            retorno = definir_tempo()
            pause = False
            if retorno:
                tempo = tempo_padrao.copy()

        if event == 'Return:36' or event == 'iniciar':
            pause = False
            if zerado:
                tempo = tempo_padrao.copy()
                zerado = False
        if event == 'pausar':
            pause = True
        if event == 'resetar':
            pause = True
            tempo = tempo_padrao.copy()

        tempo = atualizar_horario(tempo)
        t_hora, t_min, t_seg = int(tempo["hora"]), int(tempo["min"]), int(tempo["seg"])
        text.update(f'{str(set_num(t_hora))}:{str(set_num(t_min))}:{str(set_num(t_seg))}')
        if t_hora == 0 and t_min == 0 and t_seg == 0:
            zerado = True
        if t == 2:
            t = 0
            tempo['seg'] = int(tempo['seg']) - 1
        if not pause:
            t = t + 1

    win.close()

if __name__ == "__main__":
    janela_principal()
    #definir_tempo()
