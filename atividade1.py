class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def detalhes_do_curso(self):
        return f"Curso: {self.nome}\nDuração: {self.duracao} anos"


class Presencial(Curso):
    def __init__(self, nome, duracao, numero_de_vagas):
        super().__init__(nome, duracao)
        self.numero_de_vagas = numero_de_vagas

    def detalhes_do_curso(self):
        return f"{super().detalhes_do_curso()}\nVagas Disponíveis: {self.numero_de_vagas}"


class Online(Curso):
    def __init__(self, nome, duracao, plataforma_online):
        super().__init__(nome, duracao)
        self.plataforma_online = plataforma_online

    def detalhes_do_curso(self):
        return f"{super().detalhes_do_curso()}\nPlataforma Online: {self.plataforma_online}"


# Exemplo de uso
curso_presencial = Presencial("Curso de Python", 2, 30)
curso_online = Online("Curso de Machine Learning", 1, "Coursera")

print(curso_presencial.detalhes_do_curso())
print("\n")
print(curso_online.detalhes_do_curso())
