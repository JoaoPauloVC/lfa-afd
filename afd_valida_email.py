class ValidadorEmail:
    def __init__(self):
        self.estado_atual = 0

    def validar(self, email):
        self.estado_atual = 0

        transicoes = {
            0: {"alfanumero": 1},
            1: {"alfanumero": 1, "caractere_especial": 1, ".": 2, "@": 3},
            2: {"alfanumero": 1, "caractere_especial": 1},
            3: {"alfanumero": 4},
            4: {"alfanumero": 4, ".": 5},
            5: {"alfanumero": 5, ".": 6},
            6: {"alfanumero": 5}
        }

        for caractere in email:
            categoria = self._get_categoria(caractere)
            if categoria in transicoes[self.estado_atual]:
                self.estado_atual = transicoes[self.estado_atual][categoria]
            else:
                return False  

        return self.estado_atual in [5]

    def _get_categoria(self, caractere):
        if caractere.isalnum():
            return 'alfanumero'
        elif (caractere == '-' or caractere == '_'):
            return 'caractere_especial'
        elif caractere == '.':
            return "."
        elif caractere == '@':
            return '@'



# Testando o ValidadorEmail

validador_teste = ValidadorEmail()
emails = ["meu_email@provedor.com.br", "usuario@example.com", "email_invalido@", "@sem_usuario.com", "sem_arroba.com"]

print(f'Os e-mails abaixo são exemplos Básicos:')
for email in emails:
    if validador_teste.validar(email):
        print(f'O e-mail "{email}" é válido.')
    else:
        print(f'O e-mail "{email}" é inválido.')

validador = ValidadorEmail()

print("Agora é sua vez!")
while True:
    email = input("Digite o endereço de e-mail (ou digite 'exit' para sair): ")
    if email.lower() == 'exit':
        print("Encerrando o programa...")
        break

    if validador.validar(email):
        print(f'O e-mail "{email}" é válido.')
    else:
        print(f'O e-mail "{email}" é inválido.')
