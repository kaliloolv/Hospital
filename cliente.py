class cliente:
    dic={}

    def _init_(self,nome,idade,crm,numero): #caracteristicas do usuario.
        self.nome = nome
        self.idade = idade
        self.crm = crm
        self.numero = numero

    def Cadastrarpaciente(self):
        self.dic[self.nome] = {"nome":self.nome}, {"idade": self.idade}, {"crachá": self.crm}, {"Contato": self.numero}

    def Listarpaciente(self,nome):
        try:
            nomeEncontradopaciente = self.dic[nome]
        except (KeyError):
            print("nome não foi ")
        else:
            return nomeEncontradopaciente
