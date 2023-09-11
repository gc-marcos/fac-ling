class FuncionarioTecnico:
    nivel = 'Técnico'  # Atributo de classe

    def __init__(self, status):
        self.status = status
func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')

print(FuncionarioTecnico.nivel)  # Acessando o atributo de classe nivel
print(func1.nivel)  # Isso também funcionaria, mas é preferível usar o nome da classe
print(func2.nivel)  # Mesma observação aqui
print(func1.status)
