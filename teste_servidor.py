#importação das classes
from cadastro import Cadastro
from pessoa import Pessoa
from paciente import Paciente
from recepcionista import Recepcionista
from login import Login
from medico import Medico
from funcionario import Funcionario
from admin import Admin
from atendimento import Guiche
from consulta import Consulta
from medico_BDmysql import MedicoFunc
from impressao import Imprimir

import socket
host = 'localhost'
port = 8008
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)
print("Aguardando conexão...")
conexao_servidor, cliente = serv_socket.accept()
print("Conectado")


#importação do banco de dados
import mysql.connector

# configurações da conexão com o banco de dados 
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'clinica',
    'raise_on_warnings': True
}

login_atual = ''
senha_atual = ''
login_atual_Recep = ''
senha_atual_Recep = ''

try:
    # conectar com o banco de dados
    conexao = mysql.connector.connect(**config)
    print('Conexão realizada com sucesso!')

    # criando cursor para executar consultas
    cursor = conexao.cursor()


    class BancoDeDados:
        def __init__(self):
            # configurações da conexão com o banco de dados 
            self.connection = mysql.connector.connect(
                user = 'root',
                password = '',
                host = 'localhost',
                database = 'mydb',
        )
            self.cad = Cadastro()
            self.log = Login()
            self.gui = Guiche()
            self.imp = Imprimir()
            self.consult = Consulta()
            self.med = MedicoFunc()
            
        def processarDados(self, recebe):
            self.connection.commit()
            dados = recebe.decode().split(",")
            if len(dados) >= 1:
                acao = dados[0]
                if acao.lower() == 'admin':
                    self.loginAdmin(dados[1],dados[2])
                elif acao.lower() == 'medico':
                    self.loginMedico(dados[1],dados[2])
                elif acao.lower() == 'recepcionista':
                    self.loginRecep(dados[1],dados[2])
                elif acao.lower() == 'cad_medicologin':
                    self.cadastroMedicoLogin(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'cad_medico':
                    self.cadastroMedico(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9])
                elif acao.lower() == 'cad_receplogin':
                    self.cadastroRecepLogin(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6])
                elif acao.lower() == 'cad_recep':
                    self.cadastroRecep(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6])
                elif acao.lower() == 'cad_admin':
                    self.cadastroAdmin(dados[1],dados[2],dados[3])
                elif acao.lower() == 'atendimento':
                    self.iniciarAtendimento()
                elif acao.lower() == 'finalizar_atendimento':
                    self.FinalizarAtendimento()
                elif acao.lower() == 'adicionaguiche':
                    self.addGuiche(dados[1],dados[2],dados[3])
                elif acao.lower() == 'excluiguiche':
                    self.excluirGuiche()
                elif acao.lower() == 'ativarguiche':
                    self.ativarGuiche()
                elif acao.lower() == 'desativarguiche':
                    self.desativarGuiche()
                elif acao.lower() == 'imprecep':
                    self.imprimirRecep(dados[1])
                elif acao.lower() == 'impmedico':
                    self.imprimirMedico(dados[1])
                elif acao.lower() == 'realizarconsult':
                    self.realizarConsulta(dados[1],dados[2],dados[3],dados[4],dados[5],dados[6],dados[7],dados[8],dados[9],dados[10])
                elif acao.lower() == 'enviarconsult':
                    self.enviarConsulta() 
                elif acao.lower() == 'busconsult':
                    self.buscConsult(dados[1])  
                elif acao.lower() == 'excluirconsult':
                    self.excluirConsult(dados[1])
                elif acao.lower() == 'verificartipo':
                    self.verificarTipo(dados[1])
                elif acao.lower() == 'bconsult':
                    self.buscCons(dados[1])
                elif acao.lower() == 'atualizaconsult':
                    self.atualizarConsult(dados[1])
                elif acao.lower() == 'listapacientes':
                    self.listaPacientes()
                elif acao.lower() == 'excluipaciente':
                    self.excluiPacientes()
               
                
                   
                
                elif acao.lower() == 'logrecp':
                    self.realCons()
                

                elif acao.lower() == 'rconsult':
                    self.realizarConsultaAA(dados[1])

                
               
                
                
                
                
               

        def loginAdmin(self,cpf,password):
            try:
                result = self.log.fazerLoginAdmin(cpf, password)
                print(result)
                conexao.commit()
                if self.log.fazerLoginAdmin(cpf,password):
                    # abre a tela de médico
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o login')
                serv_socket.close()
        
        def loginMedico(self,cpf,password):
            try:
                result = self.log.fazerLoginMed(cpf, password)
                print(result)
                conexao.commit()
                if self.log.fazerLoginMed(cpf,password):
                    global login_atual 
                    login_atual= cpf
                    global senha_atual
                    senha_atual = password
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o login')
                serv_socket.close()
        
        def loginRecep(self,cpf,password):
            try:
                result = self.log.fazerLoginRecep(cpf, password)
                print(result)
                conexao.commit()
                if self.log.fazerLoginRecep(cpf,password):
                    global login_atual_Recep
                    login_atual_Recep = cpf
                    global senha_atual_Recep
                    senha_atual_Recep = password
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o login')
                serv_socket.close()
        
        def cadastroMedicoLogin(self,cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):
            try:
                result = self.cad.cadastroMedico(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroMedico(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()

        def cadastroMedico(self,cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha):
            try:
                result = self.cad.cadastroMedico(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroMedico(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO medico(cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,especialidade,hr_atendimento,crm,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def cadastroRecepLogin(self,cpf,nome,telefone,dt_nasc,email,senha):
            try:
                result = self.cad.cadastroRecep(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroRecep(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,senha) VALUES(%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def cadastroRecep(self,cpf,nome,telefone,dt_nasc,email,senha):
            try:
                result = self.cad.cadastroRecep(cpf)
                #print(retorno)
                print(result)
                if self.cad.cadastroRecep(cpf):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO recepcionista(cpf,nome,telefone,dt_nasc,email,senha) VALUES(%s,%s,%s,%s,%s,%s)"
                    values = (cpf,nome,telefone,dt_nasc,email,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def cadastroAdmin(self,cpf_admin, nome, senha):
            try:
                result = self.cad.cadastroAdmin(cpf_admin)
                #print(retorno)
                print(result)
                if self.cad.cadastroAdmin(cpf_admin):
                    # utilizando comandos SQL para realizar as inserções no banco de dados
                    query = "INSERT INTO admin(cpf_admin,nome,senha) VALUES(%s,%s,%s)"
                    values = (cpf_admin,nome,senha)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(query, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '3'
                        conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def iniciarAtendimento(self):
            try:
                result = self.gui.iniciar_atendimento(login_atual_Recep)
                if result == None:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                elif result == False:
                    enviar = '3' 
                    conexao_servidor.send(enviar.encode())
                elif result == True:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = f'{result}'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()

        def FinalizarAtendimento(self):
            try:
                result = self.gui.finalizar_atendimento(login_atual_Recep)
                if result == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                elif result == True:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = f'{result}'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def addGuiche(self,status,senha,modo):
            try:
                conexao.commit()
                consulta = "SELECT recepcionista_cpf FROM guiche WHERE recepcionista_cpf = %s"
                cursor.execute(consulta,(login_atual_Recep,))
                resultado = cursor.fetchone()
                print(resultado)
                if resultado:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                else:
                    guiche = "INSERT INTO guiche(status,senha,modo,recepcionista_cpf) VALUES(%s,%s,%s,%s)"
                    values = (status,senha,modo,login_atual_Recep)
                    try:
                        # utilizando o cursor para executar a inserção no banco de dados
                        cursor.execute(guiche, values)
                        #confirmar a inserção
                        conexao.commit()
                        enviar = '1'
                        conexao_servidor.send(enviar.encode())
                    except mysql.connector.errors.IntegrityError:
                        enviar = '2'
                        conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def excluirGuiche(self):
            try:
                consulta = "SELECT id_guiche FROM guiche WHERE recepcionista_cpf = %s"
                cursor.execute(consulta,(login_atual_Recep,))
                resultado = cursor.fetchone()
                print(resultado)
                result = self.gui.excluir_guiche(resultado[0])
                if result == True:
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif result == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def ativarGuiche(self):
            try:
                consulta = "SELECT id_guiche FROM guiche WHERE recepcionista_cpf = %s"
                cursor.execute(consulta,(login_atual_Recep,))
                resultado = cursor.fetchone()
                print(resultado)
                result = self.gui.ativarGuiche(resultado[0])
                if result == True:
                    ativar = "UPDATE guiche SET modo = 'ativo' WHERE id_guiche = %s"
                    cursor.execute(ativar,(resultado[0],))
                    conexao.commit()
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif result == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()

        def desativarGuiche(self):
            try:
                consulta = "SELECT id_guiche FROM guiche WHERE recepcionista_cpf = %s"
                cursor.execute(consulta,(login_atual_Recep,))
                resultado = cursor.fetchone()
                print(resultado)
                result = self.gui.desativarGuiche(resultado[0])
                if result == True:
                    desativar = "UPDATE guiche SET modo = 'inativo' WHERE id_guiche = %s"
                    cursor.execute(desativar,(resultado[0],))
                    #confirmar a inserção
                    conexao.commit()
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif result == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def imprimirRecep(self,cpf):
            try:
                pessoa = self.imp.buscRecep(cpf)
                if (pessoa != None):
                    cursor.execute('SELECT nome FROM recepcionista WHERE cpf = %s', (pessoa,))
                    nome = cursor.fetchone()[0]
                    cursor.execute('SELECT telefone FROM recepcionista WHERE cpf = %s', (pessoa,))
                    telefone = cursor.fetchone()[0]
                    cursor.execute('SELECT dt_nasc FROM recepcionista WHERE cpf = %s', (pessoa,))
                    dt_nasc = cursor.fetchone()[0]
                    cursor.execute('SELECT email FROM recepcionista WHERE cpf = %s', (pessoa,))
                    email = cursor.fetchone()[0]
                    cursor.execute('SELECT senha FROM recepcionista WHERE cpf = %s', (pessoa,))
                    senha = cursor.fetchone()[0]
                    conexao.commit()
                    enviar = f'1,{nome},{telefone},{dt_nasc},{email},{senha}'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def imprimirMedico(self, cpf):
            try:
                pessoa = self.imp.buscMed(cpf)
                if (pessoa != None):
                    cursor.execute('SELECT nome FROM medico WHERE cpf = %s', (pessoa,))
                    nome = cursor.fetchone()[0]
                    cursor.execute('SELECT telefone FROM medico WHERE cpf = %s', (pessoa,))
                    telefone = cursor.fetchone()[0]
                    cursor.execute('SELECT dt_nasc FROM medico WHERE cpf = %s', (pessoa,))
                    dt_nasc = cursor.fetchone()[0]
                    cursor.execute('SELECT email FROM medico WHERE cpf = %s', (pessoa,))
                    email = cursor.fetchone()[0]
                    cursor.execute('SELECT especialidade FROM medico WHERE cpf = %s', (pessoa,))
                    especialidade = cursor.fetchone()[0]
                    cursor.execute('SELECT hr_atendimento FROM medico WHERE cpf = %s', (pessoa,))
                    hr_atendimento = cursor.fetchone()[0]
                    cursor.execute('SELECT crm FROM medico WHERE cpf = %s', (pessoa,))
                    crm = cursor.fetchone()[0]
                    cursor.execute('SELECT senha FROM medico WHERE cpf = %s', (pessoa,))
                    senha = cursor.fetchone()[0]
                    enviar = f'1,{nome},{telefone},{dt_nasc},{email},{especialidade},{hr_atendimento},{crm},{senha}'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()

        def realizarConsulta(self,cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,qtd_vagas,cpf_medico,cpf_recepcionista):
            result = self.consult.verificaMedico(medico,crm,cpf_medico)
            resultado = self.consult.verificaRecep(cpf_recepcionista)
            #print(retorno)
            print(result)
            print(resultado)
            if result == None and resultado == None:
                enviar = '3'
                conexao_servidor.send(enviar.encode())
            elif result == None:
                enviar = '4'
                conexao_servidor.send(enviar.encode())
            elif resultado == None:
                enviar = '5'
                conexao_servidor.send(enviar.encode())
            else:
                print('nao retornou NONE')
               
                # utilizando comandos SQL para realizar as inserções no banco de dados
                query = "INSERT INTO consulta(cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo_consulta,qtd_vagas,medico_cpf,recepcionista_cpf) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (cpf_paciente,nome_paciente,telefone,dt_nasc,medico,crm,tipo,qtd_vagas,cpf_medico,cpf_recepcionista)
                try:
                    # utilizando o cursor para executar a inserção no banco de dados
                    cursor.execute(query, values)
                    #confirmar a inserção
                    conexao.commit()
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                except mysql.connector.errors.IntegrityError:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())


        def proxima(self):
            pass

        def realCons(self):
            try:
                cursor.execute("SELECT nome FROM medico")
                listaMed = cursor.fetchall()
                dados = ','.join([item[0] for item in listaMed])
                enviar = f'{login_atual_Recep},{dados}'
                conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()

        def realizarConsultaAA(self, medico):
            try:
                cursor.execute("SELECT cpf, crm FROM medico WHERE nome = %s",(medico,))
                listaMed = cursor.fetchall()
                print(listaMed)
                
                cursor.execute("SELECT qtd_vagas FROM consulta WHERE medico_cpf = %s",(listaMed[0][0],))
                paciente = cursor.fetchall()
                print(paciente)

                if len(paciente) > 0:
                    enviar = f'1,{listaMed[0][0]},{str(listaMed[0][1])},{str(paciente[0][0])}'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = f'2,{listaMed[0][0]},{str(listaMed[0][1])}'
                    conexao_servidor.send(enviar.encode())



            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def enviarConsulta(self):
            conexao.commit()
            try:
                result = self.consult.enviar_consulta(login_atual_Recep)
                if result == False:
                    enviar = '3'
                    conexao_servidor.send(enviar.encode())
                elif result == 2:
                    enviar = '4'
                    conexao_servidor.send(enviar.encode())
                elif result == 3:
                    enviar = '5'
                    conexao_servidor.send(enviar.encode())
                elif result == 4:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())
                elif result == True:
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif result == 0:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = result
                    conexao_servidor.send(enviar.encode())


            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def buscConsult(self,cpf):
            try:
                conexao.commit()
                pessoa = self.consult.buscConsulta(cpf)
                print(pessoa)
                if (pessoa != None):
                    print('entrou na seleção')
                    cursor.execute('SELECT nome_paciente FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    nome = cursor.fetchone()[0]
                    cursor.execute('SELECT telefone FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    telefone = cursor.fetchone()[0]
                    cursor.execute('SELECT dt_nasc FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    dt_nasc = cursor.fetchone()[0]
                    cursor.execute('SELECT medico FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    medico = cursor.fetchone()[0]
                    cursor.execute('SELECT crm FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    crm = cursor.fetchone()[0]
                    cursor.execute('SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    tipo_consulta = cursor.fetchone()[0]
                    cursor.execute('SELECT qtd_vagas FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    qtd_vagas = cursor.fetchone()[0]
                    cursor.execute('SELECT medico_cpf FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    cpf_medico = cursor.fetchone()[0]
                    cursor.execute('SELECT recepcionista_cpf FROM consulta WHERE cpf_paciente = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,))
                    cpf_recepcionista = cursor.fetchone()[0]
                    enviar = f'1,{nome},{telefone},{dt_nasc},{medico},{crm},{tipo_consulta},{qtd_vagas},{cpf_medico},{cpf_recepcionista}'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def excluirConsult(self,cpf):
            try:
                result = self.consult.excluir_consulta(cpf) 
                if result == True:
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif result == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                elif result == None:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def verificarTipo(self,cpf):
            try:
                retorno = self.consult.verificar_tipo(cpf)
                if retorno == True:
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif retorno == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                elif retorno == None:
                    enviar = '3'
                    conexao_servidor.send(enviar.encode())
                
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def buscCons(self,cpf):
            try:
                conexao.commit()
                pessoa = self.med.buscarPacientes(cpf, login_atual)
                print(pessoa)
                if (pessoa != None):              
                    cursor.execute('SELECT nome_paciente FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1 ', (pessoa,login_atual,))
                    nome = cursor.fetchone()[0]
                    cursor.execute('SELECT telefone FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    telefone = cursor.fetchone()[0]
                    cursor.execute('SELECT dt_nasc FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    dt_nasc = cursor.fetchone()[0]
                    cursor.execute('SELECT medico FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    medico = cursor.fetchone()[0]
                    cursor.execute('SELECT crm FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    crm = cursor.fetchone()[0]
                    cursor.execute('SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    tipo_consulta = cursor.fetchone()[0]
                    cursor.execute('SELECT qtd_vagas FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    qtd_vagas = cursor.fetchone()[0]
                    cursor.execute('SELECT medico_cpf FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    cpf_medico = cursor.fetchone()[0]
                    cursor.execute('SELECT recepcionista_cpf FROM consulta WHERE cpf_paciente = %s AND medico_cpf = %s ORDER BY id_consulta DESC LIMIT 1', (pessoa,login_atual,))
                    cpf_recepcionista = cursor.fetchone()[0]
                    print('saiu daqui')
                    enviar = f'1,{nome},{telefone},{dt_nasc},{medico},{crm},{tipo_consulta},{qtd_vagas},{cpf_medico},{cpf_recepcionista}'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())

            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def atualizarConsult(self, cpf):
            try:
                result = self.med.atualizaConsulta(cpf,login_atual)
                if result == True:
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                elif result == False:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                elif result == None:
                    enviar = '2'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor durante o cadastro do medico')
                serv_socket.close()
        
        def listaPacientes(self):
            try:
                self.cursor.execute("SELECT cpf, nome FROM lista_pacientes WHERE medico_cpf = %s",(login_atual,))
                lista = self.cursor.fetchall()
                print('lista:',lista)
                if len(lista) != 0:
                    dados = ''
                    for item in lista:
                        cpf, nome = item
                        dados += f'CPF: {cpf}, Nome: {nome}\n'
                    conexao_servidor.send(dados.encode())
                    """
                    dados = ','.join([item[0] for item in lista])
                    enviar = f'{dados}'
                    #enviar = f'{lista[0][0]}'
                    conexao_servidor.send(enviar.encode())
                    """
                else:
                    enviar = 'Sem pacientes'
                    #enviar = f'{lista[0][0]}'
                    conexao_servidor.send(enviar.encode())
            except:
                print('Erro do servidor')
                #serv_socket.close()

        def excluiPacientes(self):
            try:
                selecione = "SELECT * FROM lista_pacientes ORDER BY id_paciente LIMIT 1"
                cursor.execute(selecione)
                resultado = cursor.fetchone()   

                print(resultado)
                
                if resultado is not None:
                    excluido = "DELETE FROM lista_pacientes WHERE id_paciente = %s"
                    print(resultado[0])
                    cursor.execute(excluido, (resultado[0],))
                    print(resultado[0])
                    print('excluiu')
                    #pacientes = cursor.fetchone()
                    conexao.commit()
                    enviar = '1'
                    conexao_servidor.send(enviar.encode())
                else:
                    enviar = '0'
                    conexao_servidor.send(enviar.encode())
                        
            except:
                print('Erro do servidor ')
                serv_socket.close()

            
                

            
               
               


except mysql.connector.Error as erro:
    print(f'Eroo ao conectar o Banco de Dados: {erro}')

if __name__ == "__main__":
    bd = BancoDeDados()
    while True:
        recebe = conexao_servidor.recv(1024)
        if not recebe:
            break  # Encerra o loop se não houver mais mensagens
        
        print("Mensagem recebida: " + recebe.decode())
        bd.processarDados(recebe)
    conexao_servidor.close()
    