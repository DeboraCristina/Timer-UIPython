def set_num(n = 0):
    if int(n) < 10:
        n = f'0{int(n)}'
    return n

def atualizar_horario(horario = None):
    if horario == None or len(horario) != 3:
        return
    if ('hora' not in horario) or ('min' not in horario) or ('seg' not in horario):
        return
    chave=list(horario.keys())
    h, m, s = int(horario[chave[0]]), int(horario[chave[1]]), int(horario[chave[2]])
    if h <= 0 and m <= 0 and s <= 0:
        return {chave[0]:'00', chave[1]:'00', chave[2]:'00'}
    if m >= 0:
        if s < 0:
            m = m - 1
            s = 59
    if h >= 0:
        if m < 0:
            h = h - 1
            m = 59
    horario[chave[0]] = str(set_num(h))
    horario[chave[1]] = str(set_num(m))
    horario[chave[2]] = str(set_num(s))
    return horario

