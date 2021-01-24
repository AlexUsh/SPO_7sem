from lexer import Lexer
from parser import Parser
from transfer import PN
from stack_machine import stack_machine
from triad_processing import Triad

f = open('language.txt')
inp = f.read()
f.close()

print('\nLexer result output: ')
l = Lexer()
tokens = l.lex(inp)

p = Parser(tokens)
pars = p.lang()
print('\nParser result output: ', pars)

if pars:
    pn = PN(tokens)
    transfer, fun = pn.transfer_PN()

    tr = Triad(transfer, fun)
    t, val = tr.triad_op()

    for i in range(len(fun)):
        print("\nTriads processing process: ")
        triad = Triad(fun[i][-1], fun)
        fun[i][-1] = triad.triad_op(False)

    sm = stack_machine(t, val, fun)
    thread_flag = 'n'
   
    sm.stack_machine_run()
