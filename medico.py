class medico:
    dic={}

    def _init_(self,nome,idade,crm,numero): #caracteristicas do usuario.
        self.nome = nome
        self.idade = idade
        self.crm = crm
        self.numero = numero

    def CadastrarMedico(self):
        self.dic[self.nome] = {"nome":self.nome}, {"idade": self.idade}, {"crachá": self.crm}, {"Contato": self.numero}

    def ListarMedico(self,nome):
        try:
            nomeEncontradomedico = self.dic[nome]
        except (KeyError):
            print("nome não existe.")
        else:
            return nomeEncontradomedico