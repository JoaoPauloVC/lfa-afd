class ValidadorEmail:
    def __init__(self):
        self.estado_atual = 0

    def validar(self, email):
        transicoes = {
            0: {'letras_digitos': 1},
            1: {'letras_digitos': 1, '.': 2, '-': 2, '_': 2},
            2: {'letras': 3},
            3: {'letras': 3, '.': 4},
            4: {'letras': 5},
            5: {'letras': 5}
        }

        for caractere in email:
            categoria = self._get_categoria(caractere)
            if categoria in transicoes[self.estado_atual]:
                self.estado_atual = transicoes[self.estado_atual][categoria]
            else:
                return False

        return self.estado_atual in [3, 5]

    def _get_categoria(self, caractere):
        if caractere.isalnum():
            return 'letras_digitos'
        elif caractere == '.':
            return '.'
        elif caractere == '-':
            return '-'
        elif caractere == '_':
            return '_'
        else:
            return 'letras'


# Testando o ValidadorEmail
validador = ValidadorEmail()
emails = ["usuario@example.com", "meu_email@provedor.com.br", "email_invalido@", "@sem_usuario.com", "sem_arroba.com"]

for email in emails:
    print(f'{email}: {validador.validar(email)}')
