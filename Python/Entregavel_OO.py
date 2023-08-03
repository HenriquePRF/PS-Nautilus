import pandas #Usado para imprimir tabela no terminal

class AUV: #Define uma classe para conter os AUVs
    lista_de_auvs = [] #lista com todos os AUVs

    def __init__(self, thrusters: int, sensores: list, ano: int, nome: str, teamsize: int): #Define os dados dos AUVs
        self.thrusters = thrusters
        self.sensores = sensores
        self.ano = ano 
        self.nome = nome
        self.teamsize = teamsize
        AUV.lista_de_auvs.append(self)  # Adiciona a instancia criada a lista de todos os AUVs

    def tabela(self): #Para imprimir uma tabela com os AUVs e seus dados no terminal
        data = {
            'Nome': [auv.nome for auv in AUV.lista_de_auvs],
            'Ano': [auv.ano for auv in AUV.lista_de_auvs],
            'Thrusters': [auv.thrusters for auv in AUV.lista_de_auvs],
            'Sensores': [', '.join(auv.sensores) for auv in AUV.lista_de_auvs],
            'Teamsize': [auv.teamsize for auv in AUV.lista_de_auvs]
        }
        return pandas.DataFrame(data)

    def informacoes(self): #Para exibir as informacoes de um AUV individualmente
        print("Informacoes do Robo:")
        print(f"Nome: {self.nome}")
        print(f"Ano: {self.ano}")
        print(f"Numero de Thrusters: {self.thrusters}")
        print("Sensores:")
        for sensor in self.sensores:
            print(f"- {sensor}")
        print(f"Tamanho da equipe: {self.teamsize}")
        print()

    def rank_ano(self): #Ordena os AUVs em ordem crescente de idade e retorna essa lista
        lista_ordenada = sorted(AUV.lista_de_auvs, key=lambda auv: auv.ano, reverse=True)
        return lista_ordenada
    
    def rank_equipe(self): #Ordena os AUVs em ordem crescente de tamanho de equipe e retorna essa lista
        lista_ordenada = sorted(AUV.lista_de_auvs, key=lambda auv: auv.teamsize, reverse=True)
        return lista_ordenada

lua = AUV(thrusters= 6, sensores=["Camera", "DVL sensor", "BAR30", "BMP180", "Hydrophone"], ano=2022, nome="Lua",teamsize=42) #Aloca valores para os diferentes dados da Lua
brhue = AUV(thrusters= 6, sensores=["Camera", "Hydrophone","IMU","Depth sensor"], ano=2020, nome="BrHUE",teamsize=35) #Aloca valores para os diferentes dados do BrHUE

print(lua.tabela()) #Imprime a tabela com os dados de todos AUVs
for auv in AUV.lista_de_auvs:
    auv.informacoes()

print("AUVs do mais novo ao mais antigo:") #Imprime lista rankeado de mais novo ate mais velho
for auv in lua.rank_ano():
    print(f"{auv.nome} - Ano {auv.ano}")

print("AUVs com a maior equipe ao com a menor equipe:")  #Imprime lista rankeado de maior equipe are menor
for auv in lua.rank_equipe():
    print(f"{auv.nome} - Equipe de {auv.teamsize} pessoas")


'''

Implemente um modelo que descreva os AUVs da UFRJ Nautilus

Requerimentos

Deve conter os atributos: número de thursters, lista com sensores, ano de
construção, nome do veículo, e no mínimo, mais 1 atributo de livre escolha
Deve conter métodos para:
◦ Exibir todos os AUVs em tabela
◦ Exibir os robôs individulmente
◦ Rankear os robôs do mais novo para o mais antigo
Deve conter outro método de livre escolha

'''