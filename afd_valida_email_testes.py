# Para ter um endereço válido:
    # 1) Nome de usuário (retirado, com adaptações, do Wikipedia, referência no artigo):
        # Letras Latinas "A" a "Z" e "a" a "z"
        # Dígitos de 0 a 9
        # Caracteres especiais: _, -, .
        # Atenção: o ponto "." não pode ser o primeiro nem último caractere fornecido e também não pode aparecer consecutivamente
        
    # 2) Domínio:
        # Letras Latinas "A" a "Z" e "a" a "z"
        # Dígitos de 0 a 9, fornecido que o TLD (top-level domain) não seja todo numérico
        # Hifén, garantido que não é o primeiro nem último caractere

class ValidadorEmail:
    def __init__(self):
        self.estado_atual = 0
        self.dominio = False

    def validar(self, email):
        self.estado_atual = 0
        self.dominio = False

        transicoes = {
            # 0:{"dominio_letra_numero":1, ""}



            0: {'letra_numero': 1, 'caractere_especial': 1},  # Estado 0: Garante 1 caractere antes de @
            1: {'letra_numero': 1, 'caractere_especial': 1, '@': 2},  # Estado 1: Outros caracteres. @ leva ao domínio
            2: {'letras': 2, '.': 3},  # Estado 1: Domínio do E-mail (google,yahoo, etc.). Muda para Estado 2 com .
            3: {'letras': 3, '.': 4},  # Estado 2: Parte "com" do e-mail. Pode ser que haja subdomínio (.br, por exemplo). Muda para Estado 3 com .
            4: {'letras': 4},  # Estado 3: Transição para o estado 4 com letras após o último ponto
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
        # Retorna True se o estado atual do autômato estiver em estado final (2,3), indicando que o e-mail é válido
        return self.estado_atual in [3,4]

    def _get_categoria(self, caractere):
        # Retorna a categoria do caractere
        if caractere.isalnum() and not self.dominio:
            return 'letra_numero'
        elif (caractere == '.' or caractere == '-' or caractere == '_') and not self.dominio:
            return 'caractere_especial'
        elif caractere == '@':
            self.dominio = True
            return '@'
        elif caractere == '.' and self.dominio:
            return '.'
        else:
            return 'letras'

# Testando o ValidadorEmail

validador_teste = ValidadorEmail()
emails = ["usuario@example.com", "meu_email@provedor.com.br", "email_invalido@", "@sem_usuario.com", "sem_arroba.com"]

print(f'Os e-mails abaixo são exemplos Básicos:')
for email in emails:
    # Valida cada endereço de e-mail e imprime o resultado na tela
    if validador_teste.validar(email):
        print(f'O e-mail "{email}" é válido.')
    else:
        print(f'O e-mail "{email}" é inválido.')

validador = ValidadorEmail()

# Loop infinito para solicitar entrada do usuário até que o programa seja cancelado
print("Agora é sua vez!")
while True:
    # Solicita ao usuário que digite um e-mail
    email = input("Digite o endereço de e-mail (ou digite 'exit' para sair): ")

    # Verifica se o usuário digitou 'exit' para sair do programa
    if email.lower() == 'exit':
        print("Encerrando o programa...")
        break

    # Valida o e-mail usando o ValidadorEmail e imprime o resultado na tela
    if validador.validar(email):
        print(f'O e-mail "{email}" é válido.')
    else:
        print(f'O e-mail "{email}" é inválido.')
