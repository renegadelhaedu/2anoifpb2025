import sqlite3
from modelos import Pessoa

class PessoaDAO:
    #SGBD = sistema gerenciador de banco de dados
    #SQL = linguagem de consulta para banco de dados
    def __init__(self, banco):
        #estrutura para criar as tabelas
        self.conn = sqlite3.connect(banco)
        self.cursor = self.conn.cursor()
        self.cursor.execute(#crie se nao existir, dê o nome a tabela, crie os campos
            #em cada campo/atributo/coluna: nome_coluna, tipo, relacionamentos (restrições)
            "CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER)"
        )
        self.conn.commit()

    def inserir(self, pessoa):
        self.cursor.execute(
            "INSERT INTO pessoas (nome, idade) VALUES (?, ?)",
            (pessoa.nome, pessoa.idade)
        )
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT id, nome, idade FROM pessoas")
        #fetchall = traga tudoooo
        dados = self.cursor.fetchall()
        lista = []
        for id, nome, idade in dados:
            nova_pessoa = Pessoa(id, nome, idade) #instanciando cada objeto
            lista.append(nova_pessoa)

        return lista

    def atualizar(self, pessoa):
        self.cursor.execute(
            "UPDATE pessoas SET nome=?, idade=? WHERE id=?",
            (pessoa.nome, pessoa.idade, pessoa.id)
        )
        self.conn.commit()

    def deletar(self, id):
        self.cursor.execute("DELETE FROM pessoas WHERE id=?", (id,))
        self.conn.commit()