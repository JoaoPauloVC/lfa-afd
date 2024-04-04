class ValidadorEmail:
    def __init__(self):
        self.estado_atual = 0
        self.dominio = False

    def validar(self, email):
        transicoes = {
            0: {'letra_numero': 0, 'caractere_especial': 0, '@': 1},  # Estado 0: Nome do usuário. Muda para Estado 1 com @
            1: {'letras': 1, '.': 2},  # Estado 1: Domínio do E-mail (google,yahoo, etc.). Muda para Estado 2 com .
            2: {'letras': 2, '.': 3},  # Estado 2: Parte "com" do e-mail. Pode ser que haja subdomínio (.br, por exemplo). Muda para Estado 3 com .
            3: {'letras': 3},  # Estado 3: Transição para o estado 4 com letras após o último ponto
        }

        # Itera sobre cada caractere do endereço de e-mail fornecido
        for caractere in email:
            categoria = self._get_categoria(caractere)

            # Verifica se a categoria do caractere atual está presente nas transições possíveis para o estado atual do autômato
            if categoria in transicoes[self.estado_atual]:
                # Atualiza o estado atual do autômato de acordo com a transição definida
                self.estado_atual = transicoes[self.estado_atual][categoria]
            else:
                # Retorna False se não houver transição possível para a categoria do caractere atual
                return False

        self.estado_atual = 0
        # Retorna True se o estado atual do autômato estiver em estado final (3), indicando que o e-mail é válido
        return self.estado_atual in [2,3]

    def _get_categoria(self, caractere):
        # Retorna a categoria do caractere
        if caractere.isalnum() and not self.dominio:
            return 'letra_numero'
        elif caractere == '.' or caractere == '-' or caractere == '_':
            return '.'
        elif caractere == '@':
            self.dominio = True
            return '@'
        else:
            return 'letras'

# Testando o ValidadorEmail
validador = ValidadorEmail()
emails = ["usuario@example.com", "meu_email@provedor.com.br", "email_invalido@", "@sem_usuario.com", "sem_arroba.com"]


for email in emails:
    # Valida cada endereço de e-mail e imprime o resultado na tela
    print(f'{email}: {validador.validar(email)}')
