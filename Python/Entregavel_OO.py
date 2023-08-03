class AUV: #explicacao
    def _init_(self, thrusters: int, sensores: list, ano: int, nome: str, teamsize: int):
        self.thrusters = thrusters
        self.sensores = sensores
        self.ano = ano 
        self.nome = nome
        self.teamsize = teamsize
    def __repr__(self):
        return f"{self.nome} - Ano {self.ano}"

BrHUE = AUV(thrusters= 6, sensores=["Camera", "Hydrophone","IMU","Depth sensor"], ano=2020, nome="BrHUE",teamsize=35) 
Lua = AUV(thrusters= 6, sensores=["Camera", "DVL sensor", "BAR30", "BMP180", "Hydrophone"], ano=2022, nome="Lua",teamsize=42)


'''

Implemente um modelo que descreva os AUVs da UFRJ Nautilus

Requerimentos

Deve conter os atributos: número de thursters, lista com sensores, ano de
construção, nome do veículo, e no mínimo, mais 1 atributo de livre escolha
Deve conter métodos para:
◦ Exibir todos os AUVs em tabela
◦ Exibir os robôs individulmente
◦ Rankear os robôs do mais novo para o mais antigo
Deve conter outro método de livre escolha

'''