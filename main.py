from cmath import exp
import time
import tkinter as tk
from tkinter import messagebox as MessageBox
import tkinter
from automata.fa.nfa import NFA

nfa = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28'},
    input_symbols={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'},
    transitions={
        'q0': {'b': {'q1'},'c': {'q1'},'f': {'q1'},'g': {'q1'},'p': {'q1'},   'v': {'q2'},    'd': {'q3'},'t': {'q3'},'r': {'q3'},    'h': {'q4'},    'q': {'q5'},     'l': {'q6'},'y': {'q6'},'j': {'q6'},'k': {'q6'},'s': {'q6'},'x': {'q6'},'z': {'q6'},'w': {'q6'},'m': {'q6'},'n': {'q6'},     'a': {'q7'},'e': {'q7'},'i': {'q7'},'o': {'q7'},'u': {'q7'}},
        'q1': {'a': {'q8'},'e': {'q8'},'i': {'q8'},'o': {'q8'},'u': {'q8'},      'l': {'q9'},'r': {'q9'}},
        'q2': {'a': {'q8'},'e': {'q8'},'i': {'q8'},'o': {'q8'},'u': {'q8'},      'l': {'q9'}},
        'q3': {'a': {'q8'},'e': {'q8'},'i': {'q8'},'o': {'q8'},'u': {'q8'},      'r': {'q9'}},
        'q4': {'i': {'q8'},'u': {'q8'}},
        'q5': {'u': {'q10'}},
        'q6': {'a': {'q8'},'e': {'q8'},'i': {'q8'},'o': {'q8'},'u': {'q8'}},
        'q7': {'':  {'q13'}},
        'q8': {'':  {'q13'}},
        'q9': {'a': {'q11'},'e': {'q11'},'i': {'q11'},'o': {'q11'},'u': {'q11'}},
        'q10': {'e': {'q12'},'i':{'q12'}},
        'q11': {'':  {'q13'}},
        'q12': {'':  {'q13'}},
        'q13': {'b': {'q14'},'c': {'q14'},'f': {'q14'},'g': {'q14'},'p': {'q14'},'': {'q14'},    'v': {'q15'},'l': {'q15'},'': {'q15'},     'd': {'q16'},'t': {'q16'},'r': {'q16'},'': {'q16'},   'm': {'q17'},     'n': {'q18'},     'h': {'q19'},    'q': {'q20'},     'y': {'q21'},'j': {'q21'},'k': {'q21'},'s': {'q21'},'x': {'q21'},'z': {'q21'},'w': {'q21'},'': {'q21'},      'a': {'q22'},'e': {'q22'},'i': {'q22'},'o': {'q22'},'u': {'q22'},'y':{'q22'}},
        'q14': {'a': {'q23'},'e': {'q23'},'i': {'q23'},'o': {'q23'},'u': {'q23'},'': {'q23'},      'l': {'q24'},'r': {'q24'}},
        'q15': {'a': {'q23'},'e': {'q23'},'i': {'q23'},'o': {'q23'},'u': {'q23'},'': {'q23'},      'l': {'q24'}},
        'q16': {'a': {'q23'},'e': {'q23'},'i': {'q23'},'o': {'q23'},'u': {'q23'},'': {'q23'},'y':{'q23'},      'r': {'q24'},'': {'q24'}},
        'q17': {'b': {'q25'},'p': {'q25'}},
        'q18': {'v': {'q26'},'f': {'q26'},'s': {'q26'},'':  {'q26'}},
        'q19': {'b': {'q23'},'p': {'q23'}},
        'q20': {'u': {'q27'}},
        'q21': {'a': {'q23'},'e': {'q23'},'i': {'q23'},'o': {'q23'},'u': {'q23'},'': {'q23'}},
        'q22': {'':  {'q28'}},
        'q23': {'':  {'q28'}},
        'q24': {'a': {'q28'},'e': {'q28'},'i': {'q28'},'o': {'q28'},'u': {'q28'}},
        'q25': {'a': {'q28'},'e': {'q28'},'i': {'q28'},'o': {'q28'},'u': {'q28'}},
        'q26': {'a': {'q28'},'e': {'q28'},'i': {'q28'},'o': {'q28'},'u': {'q28'},'': {'q28'}},
        'q27': {'e': {'q28'},'i':{'q28'},'':{'q28'}},
        'q28': {'':  {'q13'},'':  {'q13'}}
    },
    initial_state='q0',
    final_states={'q28'}
)

def calculop():
    palabra=caja.get()
    T = tk.Text(ventana)
    if nfa.accepts_input(palabra):
        MessageBox.showinfo("Éxito", "Valor admitido")
    else:
        MessageBox.showerror("Error", "No válido")
        
if __name__ == "__main__":
    ventana=tk.Tk()
    ventana.geometry('300x100')
    ventana.title('Verificador de gramática en español')

    T = tk.Text(ventana)

    caja=tk.Entry(ventana)
    caja.pack(anchor="center")

    boton=tk.Button(ventana,text='Verificar',command=calculop)
    boton.pack(anchor="center")


    ventana.mainloop()
