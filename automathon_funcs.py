from automathon import DFA

Q = {'Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'}

# LEGENDA DO DICIONÁRIO 
# A = conjunto de caracteres alfanuméricos, ou seja, A = [0-9A-Za-z]
# CE = conjunto de caracteres especiais: {"_", "-"}
# @ = caractere arroba
# . = caractere ponto
sigma = {'A', 'CE', "@", "."}

delta = { 'Q0' : {'A':'Q1'},
          'Q1' : {'A':'Q1', 'CE':'Q1', '.':'Q2', '@':'Q3'},
          'Q2' : {'A':'Q1', 'CE':'Q1'},
          'Q3' : {'A':'Q4'},
          'Q4' : {'A':'Q4', '.':'Q5'},
          'Q5' : {'A':'Q5', '.':'Q6'},
          'Q6' : {'A':'Q5'}

        }
initial_state = 'Q0'
F = {'Q5'}

automata = DFA(Q, sigma, delta, initial_state, F)

valid = automata.is_valid()
print(f"O Autômato é válido?\n{valid}")

# estilo default
automata.view("afd01")