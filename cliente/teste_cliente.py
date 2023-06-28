import typing
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QTableWidget, QTableWidgetItem



#importação das telas
from cliente.tela_login import TelaLogin
from tela_medico import TelaMedico
from tela_recepcionista import TelaRecepcionista
from tela_login_medico import LoginMedico
from tela_login_recepcionista import LoginRecepcionista
from cadastrar_recepcionista import CadastrarRecep
from cadastrar_recp import CadastroRecp
from cadastrar_medico import CadastrarMedico
from cadastrar_med import CadastroMed
from tela_cadastro import TelaCadastros
from tela_atendimento import TelaAtendimento
from adicionar_guiche import AddGuiche
from finalizar_guiche import Finalizar
from ativar_guiche import AtivarGuiche
from desativar_guiche import DesativarGuiche
from imprimir_dados import ImpDados
from imprimir_medico import ImpMed
from imprimir_recepcionista import ImpRecp
#from impressao import Imprimir
from tela_consulta import TelaConsulta
from realizar_consulta import RealizarConsulta
from excluir_consulta import ExcluirConsulta
from verifica_tipo import VerificaTipo
from imprimir_pacientes import ImprimirPacientes
from excluir_pacientes import ExcluirPacientes
from excluir_guiche import ExcluirGuiche
from atualizar_consulta import AtualizarConsulta
from lista_pacientes import ListaPacientes
from login_admin import LoginAdmin
from cadastrar_admin import CadastrarAdmin
"""
login_atual = ''
senha_atual = ''
login_atual_Recep = ''
senha_atual_Recep = ''


import socket
ip = '192.168.0.118'
port = 9002
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)
"""

import socket
ip = 'localhost'
port = 8008
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(addr)



class Ui_main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640,480)
        

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow() 
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()
        self.stack13 = QtWidgets.QMainWindow()
        self.stack14 = QtWidgets.QMainWindow()
        self.stack15 = QtWidgets.QMainWindow()
        self.stack16 = QtWidgets.QMainWindow()
        self.stack17 = QtWidgets.QMainWindow()
        self.stack18 = QtWidgets.QMainWindow()
        self.stack19 = QtWidgets.QMainWindow()
        self.stack20 = QtWidgets.QMainWindow()
        self.stack21 = QtWidgets.QMainWindow()
        self.stack22 = QtWidgets.QMainWindow()
        self.stack23 = QtWidgets.QMainWindow()
        self.stack24 = QtWidgets.QMainWindow()
        self.stack25 = QtWidgets.QMainWindow()
        self.stack26 = QtWidgets.QMainWindow()
        self.stack27 = QtWidgets.QMainWindow()
        self.stack28 = QtWidgets.QMainWindow()
        self.stack29 = QtWidgets.QMainWindow()

        self.tela_login = TelaLogin()
        self.tela_login.setupUi(self.stack0)

        self.tela_login_medico = LoginMedico()
        self.tela_login_medico.setupUi(self.stack1)

        self.tela_login_recepcionista = LoginRecepcionista()
        self.tela_login_recepcionista.setupUi(self.stack2)

        self.tela_medico = TelaMedico()
        self.tela_medico.setupUi(self.stack3)

        self.tela_recepcionista = TelaRecepcionista()
        self.tela_recepcionista.setupUi(self.stack4)

        self.cadastrar_medico = CadastrarMedico()
        self.cadastrar_medico.setupUi(self.stack5)

        self.cadastrar_recepcionista = CadastrarRecep()
        self.cadastrar_recepcionista.setupUi(self.stack6)

        self.tela_cadastro = TelaCadastros()
        self.tela_cadastro.setupUi(self.stack7)

        self.cadastrar_recp = CadastroRecp()
        self.cadastrar_recp.setupUi(self.stack8)

        self.cadastrar_med = CadastroMed()
        self.cadastrar_med.setupUi(self.stack9)

        self.cadastrar_admin = CadastrarAdmin()
        self.cadastrar_admin.setupUi(self.stack10)

        self.tela_atendimento = TelaAtendimento()
        self.tela_atendimento.setupUi(self.stack11)

        self.adicionar_guiche = AddGuiche()
        self.adicionar_guiche.setupUi(self.stack12)

        self.finalizar_atendimento = Finalizar()
        self.finalizar_atendimento.setupUi(self.stack13)

        self.ativar_guiche = AtivarGuiche()
        self.ativar_guiche.setupUi(self.stack14)

        self.desativa_guiche = DesativarGuiche()
        self.desativa_guiche.setupUi(self.stack15) 

        self.imprimir_dados = ImpDados()
        self.imprimir_dados.setupUi(self.stack16)

        self.imprimir_recepcionista = ImpRecp()
        self.imprimir_recepcionista.setupUi(self.stack17)

        self.imprimir_medico = ImpMed()
        self.imprimir_medico.setupUi(self.stack18)

        #self.imprimir_funcionario = ImpFunc()
        #self.imprimir_funcionario.setupUi(self.stack19)

        self.tela_consulta = TelaConsulta()
        self.tela_consulta.setupUi(self.stack20)

        self.realizar_consulta = RealizarConsulta()
        self.realizar_consulta.setupUi(self.stack21)

        self.excluir_consulta = ExcluirConsulta()
        self.excluir_consulta.setupUi(self.stack22)

        self.verifica_tipo = VerificaTipo()
        self.verifica_tipo.setupUi(self.stack23)

        self.imprimir_pacientes = ImprimirPacientes()
        self.imprimir_pacientes.setupUi(self.stack24)

        self.excluir_pacientes = ExcluirPacientes()
        self.excluir_pacientes.setupUi(self.stack25)

        self.excluir_guiche = ExcluirGuiche()
        self.excluir_guiche.setupUi(self.stack26)

        self.atualizar_consulta = AtualizarConsulta()
        self.atualizar_consulta.setupUi(self.stack27)

        self.lista_pacientes = ListaPacientes()
        self.lista_pacientes.setupUi(self.stack28)

        self.login_admin = LoginAdmin()
        self.login_admin.setupUi(self.stack29)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)
        self.QtStack.addWidget(self.stack13)
        self.QtStack.addWidget(self.stack14)
        self.QtStack.addWidget(self.stack15)
        self.QtStack.addWidget(self.stack16)
        self.QtStack.addWidget(self.stack17)
        self.QtStack.addWidget(self.stack18)
        self.QtStack.addWidget(self.stack19)
        self.QtStack.addWidget(self.stack20)
        self.QtStack.addWidget(self.stack21)
        self.QtStack.addWidget(self.stack22)
        self.QtStack.addWidget(self.stack23)
        self.QtStack.addWidget(self.stack24)
        self.QtStack.addWidget(self.stack25)
        self.QtStack.addWidget(self.stack26)
        self.QtStack.addWidget(self.stack27)
        self.QtStack.addWidget(self.stack28)
        self.QtStack.addWidget(self.stack29)
        

class Main(QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tableWidget = QTableWidget(self)
        self.setCentralWidget(self.tableWidget)


        
        #self.med = Medico()
        # tela principal "Login"
        self.tela_login.pushButton_4.clicked.connect(self.abrirLoginAdmin)
        self.tela_login.pushButton.clicked.connect(self.abrirTelaLoginMedico)
        self.tela_login.pushButton_2.clicked.connect(self.abrirTelaLoginRecepcionista)
        self.tela_login.pushButton_3.clicked.connect(self.sair)

        # botões da tela login admin
        self.login_admin.pushButton.clicked.connect(self.loginAdmin)
        self.login_admin.pushButton_2.clicked.connect(self.abrirCadastroAdmin)
        self.cadastrar_admin.pushButton.clicked.connect(self.cadastroAdmin)
        self.cadastrar_admin.pushButton_2.clicked.connect(self.abrirLoginAdmin)
        self.login_admin.pushButton_3.clicked.connect(self.voltarLogin)

        # botões da tela login médico
        self.tela_login_medico.pushButton.clicked.connect(self.loginMedico)
        self.tela_login_medico.pushButton_2.clicked.connect(self.abrirCadastroMedico)
        self.tela_login_medico.pushButton_3.clicked.connect(self.voltarLogin)

        # botões da tela login recepcionista
        self.tela_login_recepcionista.pushButton.clicked.connect(self.loginRecep)
        self.tela_login_recepcionista.pushButton_2.clicked.connect(self.abrirCadastroRecepcionista)
        self.tela_login_recepcionista.pushButton_3.clicked.connect(self.voltarLogin)

        # tela de cadastro do medico na tela login
        self.cadastrar_medico.pushButton.clicked.connect(self.cadastroMedicoLogin)
        self.cadastrar_medico.pushButton_2.clicked.connect(self.voltarLoginMedico)

        # tela de cadastro do recepcionista na tela login
        self.cadastrar_recepcionista.pushButton.clicked.connect(self.cadastroRecepLogin)
        self.cadastrar_recepcionista.pushButton_2.clicked.connect(self.voltarLoginRecep)

        # tela do admin
        self.tela_cadastro.pushButton.clicked.connect(self.abrirCadastroRecep)
        self.cadastrar_recp.pushButton.clicked.connect(self.cadastroRecep)
        self.cadastrar_recp.pushButton_2.clicked.connect(self.voltarCadastros)
        self.tela_cadastro.pushButton_2.clicked.connect(self.abrirCadastroMed)
        self.cadastrar_med.pushButton.clicked.connect(self.cadastroMedico)
        self.cadastrar_med.pushButton_2.clicked.connect(self.voltarCadastros)
        self.tela_cadastro.pushButton_3.clicked.connect(self.abrirImpressao)
        #self.tela_cadastro.pushButton_3.clicked.connect(self.abrirCadastroFunc)
        #self.cadastrar_funcionario.pushButton.clicked.connect(self.cadastroFunc)
        #self.cadastrar_funcionario.pushButton_2.clicked.connect(self.voltarCadastros)
        self.tela_cadastro.pushButton_4.clicked.connect(self.abrirLoginAdmin)

        # tela do admin = tela de impressão
        self.imprimir_dados.pushButton.clicked.connect(self.abrirImpRecep)
        self.imprimir_dados.pushButton_2.clicked.connect(self.abrirImpMed)
        #self.imprimir_dados.pushButton_3.clicked.connect(self.abrirFunc)
        self.imprimir_dados.pushButton_4.clicked.connect(self.voltarCadastros)

            # tela de impressão = recepcionista
        self.imprimir_recepcionista.pushButton.clicked.connect(self.imprimirRecep)
        self.imprimir_recepcionista.pushButton_2.clicked.connect(self.abrirImpressao)

        # tela de impressão = medico
        self.imprimir_medico.pushButton.clicked.connect(self.imprimirMed)
        self.imprimir_medico.pushButton_2.clicked.connect(self.abrirImpressao)


        # tela do recepcionista
        #self.tela_recepcionista.pushButton.clicked.connect(self.abrirTelaCadastros)
        self.tela_recepcionista.pushButton_2.clicked.connect(self.abrirAtendimento)
        self.tela_recepcionista.pushButton_3.clicked.connect(self.abrirConsulta)
        self.tela_recepcionista.pushButton_5.clicked.connect(self.voltarLoginRecep)
        #self.tela_recepcionista.pushButton_4.clicked.connect(self.abrirImpressao)
        #self.tela_recepcionista.pushButton_5.clicked.connect(self.voltarLogin)

        # tela do recepcionista = tela de atendimento
        self.tela_atendimento.pushButton.clicked.connect(self.iniciarAtendimento)
        #self.tela_atendimento.pushButton_2.clicked.connect(self.abrirfinalizarAtendimento)
        self.tela_atendimento.pushButton_2.clicked.connect(self.finalizarAtendimento)
        self.finalizar_atendimento.pushButton.clicked.connect(self.finalizarAtendimento)
        self.finalizar_atendimento.pushButton_2.clicked.connect(self.abrirAtendimento)
        self.tela_atendimento.pushButton_3.clicked.connect(self.abrirAddGuiche)
        self.adicionar_guiche.pushButton.clicked.connect(self.addGuiche)
        self.tela_atendimento.pushButton_7.clicked.connect(self.excluirGuiche)
        self.adicionar_guiche.pushButton_2.clicked.connect(self.abrirAtendimento)
        self.tela_atendimento.pushButton_4.clicked.connect(self.ativarGuiche)
        self.tela_atendimento.pushButton_6.clicked.connect(self.desativar_Guiche)
        self.tela_atendimento.pushButton_5.clicked.connect(self.abrirTelaRecepcionista)

        # tela do recepcionista = tela de consulta
        self.tela_consulta.pushButton.clicked.connect(self.abrirRealizarConsult)
        self.realizar_consulta.pushButton.clicked.connect(self.realizarConsulta)
        self.realizar_consulta.pushButton_2.clicked.connect(self.abrirConsulta)
        self.tela_consulta.pushButton_2.clicked.connect(self.enviarConsulta)
        self.tela_consulta.pushButton_3.clicked.connect(self.abrirExcluirConsult)
        self.excluir_consulta.pushButton.clicked.connect(self.buscCons)
        self.excluir_consulta.pushButton_2.clicked.connect(self.excluirConsulta)
        self.excluir_consulta.pushButton_3.clicked.connect(self.abrirConsulta)
        self.tela_consulta.pushButton_4.clicked.connect(self.abrirTipoConsult)
        self.verifica_tipo.pushButton.clicked.connect(self.verificaTipo)
        self.verifica_tipo.pushButton_2.clicked.connect(self.abrirConsulta)
        self.tela_consulta.pushButton_5.clicked.connect(self.abrirTelaRecepcionista)

        # Tela do médico
        self.tela_medico.pushButton.clicked.connect(self.abrirListaPaciente)
        self.lista_pacientes.pushButton_2.clicked.connect(self.excluiPacientes)
        self.lista_pacientes.pushButton_3.clicked.connect(self.abrirTelaMedico)
        #self.tela_medico.pushButton_2.clicked.connect(self.abrirExcluirPac)
        #self.excluir_pacientes.pushButton.clicked.connect(self.excluirPaciente)
        #self.excluir_pacientes.pushButton_2.clicked.connect(self.abrirTelaMedico)
        self.atualizar_consulta.pushButton_3.clicked.connect(self.buscConsult)
        self.atualizar_consulta.pushButton.clicked.connect(self.atualizarConsulta)
        self.atualizar_consulta.pushButton_2.clicked.connect(self.abrirTelaMedico)
        self.tela_medico.pushButton_4.clicked.connect(self.abrirAtualizarCons)
        self.tela_medico.pushButton_3.clicked.connect(self.voltarLoginMedico)

    def loginAdmin(self):
        cpf = self.login_admin.lineEdit.text()
        password = self.login_admin.lineEdit_2.text()
        if not(cpf=='' or password==''):
            try:
                menssagem =  f'admin,{cpf},{password}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrirTelaCadastros()
                    #limpar os dados
                    self.login_admin.lineEdit.setText("")
                    self.login_admin.lineEdit_2.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Admin cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')
            

    def loginMedico(self):
        cpf = self.tela_login_medico.lineEdit.text()
        password = self.tela_login_medico.lineEdit_2.text()
        if not(cpf=='' or password==''):
            # menssagem do cliente
            try:
                menssagem =  f'medico,{cpf},{password}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrirTelaMedico()
                    #limpar os dados
                    self.tela_login_medico.lineEdit.setText("")
                    self.tela_login_medico.lineEdit_2.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Medico cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')
    
    
    def loginRecep(self):
        cpf = self.tela_login_recepcionista.lineEdit.text()
        password = self.tela_login_recepcionista.lineEdit_2.text()
        if not(cpf=='' or password==''):
            # menssagem do cliente
            try:
                menssagem =  f'recepcionista,{cpf},{password}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    self.abrirTelaRecepcionista()
                    #limpar os dados
                    self.tela_login_recepcionista.lineEdit.setText("")
                    self.tela_login_recepcionista.lineEdit_2.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ou Senha inválidos! Nenhum Recepcionista cadastrado com esses campos!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                cliente_socket.close()
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Informe todos os campos para fazer o Login')

    def cadastroMedicoLogin(self):
        cpf = self.cadastrar_medico.lineEdit.text()
        nome = self.cadastrar_medico.lineEdit_2.text()
        telefone = self.cadastrar_medico.lineEdit_3.text()
        dt_nasc = self.cadastrar_medico.lineEdit_4.text()
        email = self.cadastrar_medico.lineEdit_5.text()
        especialidade = self.cadastrar_medico.lineEdit_6.text()
        hr_atendimento = self.cadastrar_medico.lineEdit_7.text()
        crm = self.cadastrar_medico.lineEdit_8.text()
        #qtd_vagas = self.cadastrar_medico.lineEdit_9.text()
        senha = self.cadastrar_medico.lineEdit_10.text()

        # verifico se todos os dados foram preenchidos
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or especialidade=='' or hr_atendimento=='' or crm=='' or senha==''):
            # menssagem do cliente
            try:
                menssagem =  f'cad_medicologin,{cpf},{nome},{telefone},{dt_nasc},{email},{especialidade},{hr_atendimento},{crm},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_medico.lineEdit.setText("")
                    self.cadastrar_medico.lineEdit_2.setText("")
                    self.cadastrar_medico.lineEdit_3.setText("")
                    self.cadastrar_medico.lineEdit_4.setText("")
                    self.cadastrar_medico.lineEdit_5.setText("")
                    self.cadastrar_medico.lineEdit_6.setText("")
                    self.cadastrar_medico.lineEdit_7.setText("")
                    self.cadastrar_medico.lineEdit_8.setText("")
                    self.cadastrar_medico.lineEdit_10.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')

                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def cadastroMedico(self):
        # na tela do recepcionista
        cpf = self.cadastrar_med.lineEdit.text()
        nome = self.cadastrar_med.lineEdit_2.text()
        telefone = self.cadastrar_med.lineEdit_3.text()
        dt_nasc = self.cadastrar_med.lineEdit_4.text()
        email = self.cadastrar_med.lineEdit_5.text()
        especialidade = self.cadastrar_med.lineEdit_6.text()
        hr_atendimento = self.cadastrar_med.lineEdit_7.text()
        crm = self.cadastrar_med.lineEdit_8.text()
        senha = self.cadastrar_med.lineEdit_10.text()
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or especialidade=='' or hr_atendimento=='' or crm=='' or senha==''):
            # menssagem do cliente
            try:
                menssagem =  f'cad_medico,{cpf},{nome},{telefone},{dt_nasc},{email},{especialidade},{hr_atendimento},{crm},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_med.lineEdit.setText("")
                    self.cadastrar_med.lineEdit_2.setText("")
                    self.cadastrar_med.lineEdit_3.setText("")
                    self.cadastrar_med.lineEdit_4.setText("")
                    self.cadastrar_med.lineEdit_5.setText("")
                    self.cadastrar_med.lineEdit_6.setText("")
                    self.cadastrar_med.lineEdit_7.setText("")
                    self.cadastrar_med.lineEdit_8.setText("")
                    self.cadastrar_med.lineEdit_10.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')

                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')

        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')
    
    def cadastroRecepLogin(self):
        cpf = self.cadastrar_recepcionista.lineEdit.text()
        nome = self.cadastrar_recepcionista.lineEdit_2.text()
        telefone = self.cadastrar_recepcionista.lineEdit_3.text()
        dt_nasc = self.cadastrar_recepcionista.lineEdit_4.text()
        email = self.cadastrar_recepcionista.lineEdit_5.text()
        senha = self.cadastrar_recepcionista.lineEdit_6.text()
        # verifico se todos os dados foram preenchidos
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or senha==''):
            # menssagem do cliente
            try:
                menssagem =  f'cad_receplogin,{cpf},{nome},{telefone},{dt_nasc},{email},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_recepcionista.lineEdit.setText("")
                    self.cadastrar_recepcionista.lineEdit_2.setText("")
                    self.cadastrar_recepcionista.lineEdit_3.setText("")
                    self.cadastrar_recepcionista.lineEdit_4.setText("")
                    self.cadastrar_recepcionista.lineEdit_5.setText("")
                    self.cadastrar_recepcionista.lineEdit_6.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')

                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def cadastroRecep(self):
        cpf = self.cadastrar_recp.lineEdit.text()
        nome = self.cadastrar_recp.lineEdit_2.text()
        telefone = self.cadastrar_recp.lineEdit_3.text()
        dt_nasc = self.cadastrar_recp.lineEdit_4.text()
        email = self.cadastrar_recp.lineEdit_5.text()
        senha = self.cadastrar_recp.lineEdit_6.text()
        # verifico se todos os dados foram preenchidos
        if not(cpf=='' or nome=='' or telefone=='' or dt_nasc=='' or email=='' or senha==''):
            # mensssagem do cliente
            try: 
                menssagem =  f'cad_recep,{cpf},{nome},{telefone},{dt_nasc},{email},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_recp.lineEdit.setText("")
                    self.cadastrar_recp.lineEdit_2.setText("")
                    self.cadastrar_recp.lineEdit_3.setText("")
                    self.cadastrar_recp.lineEdit_4.setText("")
                    self.cadastrar_recp.lineEdit_5.setText("")
                    self.cadastrar_recp.lineEdit_6.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')

                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def cadastroAdmin(self):
        cpf_admin = self.cadastrar_admin.lineEdit.text()
        nome = self.cadastrar_admin.lineEdit_2.text()
        senha = self.cadastrar_admin.lineEdit_3.text()
        

        if not(cpf_admin=='' or nome=='' or senha==''):
            # menssagem do cliente
            try:
                menssagem =  f'cad_admin,{cpf_admin},{nome},{senha}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro realizado com sucesso!')
                    #limpar os dados
                    self.cadastrar_admin.lineEdit.setText("")
                    self.cadastrar_admin.lineEdit_2.setText("")
                    self.cadastrar_admin.lineEdit_3.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')
                
                elif recebida == '3':
                    QtWidgets.QMessageBox.information(None, 'interface', 'CPF ja cadastrado!')

                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: CPF já cadastrado!')
    
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')

    def iniciarAtendimento(self):
        # menssagem do cliente
        menssagem =  'atendimento'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        print('recebida')
        print(recebida)
        if recebida == '0':
            QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
        elif recebida == '3':
            QtWidgets.QMessageBox.critical(None, 'interface','guiche está ocupado.', QMessageBox.Ok)
        elif recebida == '2':
            QtWidgets.QMessageBox.critical(None, 'interface','guiche está Inativo.', QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, 'interface', str(recebida), QMessageBox.Ok)

            
        #self.gui.iniciar_atendimento(login_atual_Recep)

    def finalizarAtendimento(self):
        # menssagem do cliente
        menssagem =  'finalizar_atendimento'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        print('recebida')
        print(recebida)
        if recebida == '2':
            QtWidgets.QMessageBox.critical(None, 'interface','O guiche já está livre.', QMessageBox.Ok)
        elif recebida == '0':
            QtWidgets.QMessageBox.critical(None, 'interface','Esse recepcionista não foi cadastrado em nenhum guiche.', QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(None, 'interface', recebida, QMessageBox.Ok)
        #self.gui.finalizar_atendimento(login_atual_Recep)

    def addGuiche(self):
        senha = self.adicionar_guiche.lineEdit.text()
        status = self.adicionar_guiche.lineEdit_2.text()
        modo = self.adicionar_guiche.lineEdit_3.text()
        
        if not(senha=='' or status=='' or modo==''):
            # menssagem do cliente
            try:
                menssagem =  f'adicionaguiche,{status},{senha},{modo}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                print('recebida:',recebida)
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Guiche adicionado!')
                    #limpar os dados
                    self.adicionar_guiche.lineEdit.setText("")
                    self.adicionar_guiche.lineEdit_2.setText("")
                    self.adicionar_guiche.lineEdit_3.setText("")
                elif recebida == '0':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Recepcionista ja está cadastrado em um guiche')
                
                elif recebida == '2':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Não foi possivel adicionar o guiche!')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Não foi possivel adicionar o guiche!')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não adicionado! informe todos os campos.')

    def excluirGuiche(self):
        menssagem =  'excluiguiche'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        print('recebida')
        print(recebida)
        if recebida == '1':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche excluido')
        elif recebida == '0':
            QtWidgets.QMessageBox.information(None, 'interface', 'O Guiche já está ATIVO')
        elif recebida == '2':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não encontrado!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
        
        #self.gui.excluir_guiche(id_guiche)
        #self.excluir_guiche.lineEdit.setText('')
    
    def ativarGuiche(self):
            menssagem =  'ativarguiche'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode()
            print('recebida')
            print(recebida)
            if recebida == '1':
                QtWidgets.QMessageBox.information(None, 'interface', 'Guiche ATIVADO!')
            elif recebida == '0':
                QtWidgets.QMessageBox.information(None, 'interface', 'O Guiche já está ATIVO')
            elif recebida == '2':
                QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não encontrado!')
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')

    
    def desativar_Guiche(self):
        menssagem =  'desativarguiche'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        print('recebida')
        print(recebida)
        if recebida == '1':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche DESATIVADO!')
        elif recebida == '0':
            QtWidgets.QMessageBox.information(None, 'interface', 'O Guiche já está INATIVO')
        elif recebida == '2':
            QtWidgets.QMessageBox.information(None, 'interface', 'Guiche não encontrado!')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')

    def imprimirRecep(self):            
        cpf = self.imprimir_recepcionista.lineEdit_5.text()
        if not(cpf==''):
            # menssagem do cliente
            menssagem =  f'imprecep,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            print('recebida:',recebida)
            if recebida[0] == '1':
                self.imprimir_recepcionista.lineEdit_6.setText(recebida[1])
                self.imprimir_recepcionista.lineEdit_7.setText(recebida[2])
                self.imprimir_recepcionista.lineEdit_8.setText(recebida[3])
                self.imprimir_recepcionista.lineEdit_10.setText(recebida[4])
                self.imprimir_recepcionista.lineEdit_11.setText(recebida[5])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum recepcionista foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo CPF não foi preenchido! Informe um CPF.')

    def imprimirMed(self):
        cpf = self.imprimir_medico.lineEdit_5.text()
        if not(cpf==''):
            # menssagem do cliente
            menssagem =  f'impmedico,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            print('recebida:',recebida)
            if recebida[0] == '1':
                self.imprimir_medico.lineEdit_16.setText(recebida[1])
                self.imprimir_medico.lineEdit_17.setText(recebida[2])
                self.imprimir_medico.lineEdit_18.setText(recebida[3])
                self.imprimir_medico.lineEdit_19.setText(recebida[4])
                self.imprimir_medico.lineEdit_20.setText(recebida[5])
                self.imprimir_medico.lineEdit_21.setText(recebida[6])
                self.imprimir_medico.lineEdit_22.setText(str(recebida[7]))
                self.imprimir_medico.lineEdit_24.setText(recebida[8])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum medico foi registrada com este CPF.')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo CPF não foi preenchido! Informe um CPF.')
    
    def realizarConsulta(self):
        cpf_paciente = self.realizar_consulta.lineEdit.text()
        nome_paciente = self.realizar_consulta.lineEdit_2.text()
        telefone = self.realizar_consulta.lineEdit_3.text()
        dt_nasc = self.realizar_consulta.lineEdit_4.text()
        medico = self.realizar_consulta.comboBox.currentText()
        
        crm = self.realizar_consulta.lineEdit_6.text()
        tipo = self.realizar_consulta.lineEdit_7.text()
        qtd_vagas = self.realizar_consulta.lineEdit_8.text()
        cpf_medico = self.realizar_consulta.lineEdit_9.text()
        cpf_recepcionista = self.realizar_consulta.lineEdit_10.text()

    
        # verifico se todos os dados foram preenchidos
        if not(cpf_paciente=='' or nome_paciente=='' or telefone=='' or dt_nasc=='' or medico=='' or crm=='' or tipo=='' or qtd_vagas=='' or cpf_medico=='' or cpf_recepcionista==''):
            # TEM QUE VERIFICAR OS DADOS DA CHAVE ESTRANGEIRA
            # menssagem do cliente
            try:
                menssagem =  f'realizarconsult,{cpf_paciente},{nome_paciente},{telefone},{dt_nasc},{medico},{crm},{tipo},{qtd_vagas},{cpf_medico},{cpf_recepcionista}'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode()
                print('recebida',recebida)
                # servidor retorna 1 para verdadeiro e 0 para falso
                if recebida == '1':
                    QtWidgets.QMessageBox.information(None, 'interface', 'Consulta realizada com sucesso!')
                    #limpar os dados
                    self.realizar_consulta.lineEdit.setText("")
                    self.realizar_consulta.lineEdit_2.setText("")
                    self.realizar_consulta.lineEdit_3.setText("")
                    self.realizar_consulta.lineEdit_4.setText("")
                    #self.realizar_consulta.comboBox.setCurrentIndex(0)
                    self.realizar_consulta.lineEdit_6.setText("")
                    self.realizar_consulta.lineEdit_7.setText("")
                    self.realizar_consulta.lineEdit_8.setText("")
                    self.realizar_consulta.lineEdit_9.setText("")
                    self.realizar_consulta.lineEdit_10.setText("")

                elif recebida == '2':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Consulta não realizada')
                elif recebida == '3':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do MÉDICO e do RECEPCIONISTA estão errados! verifique os campos.')
                elif recebida == '4':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do MÉDICO estão errados! verifique os campos.')
                elif recebida == '5':
                    QtWidgets.QMessageBox.warning(None, "interface", 'Dados do RECEPCIONISTA estão errados! verifique os campos.')
                else:
                    QtWidgets.QMessageBox.information(None, 'interface', 'Erro de conexão cliente servidor!')
            except:
                QtWidgets.QMessageBox.information(None, 'interface', 'Erro: Impossivel de realizar consulta!')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Cadastro não realizado! informe todos os campos.')
    
    def enviarConsulta(self):
        # menssagem do cliente

        menssagem =  f'enviarconsult'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode()
        print('recebida:',recebida)
        if recebida == '1':
            QtWidgets.QMessageBox.information(None, 'interface', 'Erro: O paciente ja esta na lista de pacientes!')
        elif recebida == '2':
            QtWidgets.QMessageBox.information(None, 'interface', 'Eroo ao atualizar a quantidade de vagas de um medico no banco de dados')
        elif recebida == '3':
            QtWidgets.QMessageBox.information(None, 'interface', 'Não há mais vagas para este médico') 
        elif recebida == '4':
            QtWidgets.QMessageBox.warning(None, "interface", 'Dados do Médico estão errados! verifique os campos.') 
        elif recebida == '5':
            QtWidgets.QMessageBox.warning(None, "interface", 'O paciente já está na lista de pacientes do médico!')
        elif recebida == '0':
            QtWidgets.QMessageBox.warning(None, "interface", 'Erro: ao enviar uma consulta!')
        else:
            QtWidgets.QMessageBox.information(None, "interface", 'Paciente enviado para a lista de pacientes')
            QtWidgets.QMessageBox.information(None, 'interface', f'{recebida}')
       


    def buscCons(self):
        cpf = self.excluir_consulta.lineEdit.text()
        if not(cpf==''):
            # menssagem do usuario
            menssagem =  f'busconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            print('recebida: ',recebida)
            if recebida[0] == '1':
                self.excluir_consulta.lineEdit_2.setText(recebida[1])
                self.excluir_consulta.lineEdit_3.setText(recebida[2])
                self.excluir_consulta.lineEdit_4.setText(recebida[3])
                self.excluir_consulta.lineEdit_5.setText(recebida[4])
                self.excluir_consulta.lineEdit_6.setText(str(recebida[5]))
                self.excluir_consulta.lineEdit_7.setText(recebida[6])
                self.excluir_consulta.lineEdit_8.setText(str(recebida[7]))
                self.excluir_consulta.lineEdit_9.setText(recebida[8])
                self.excluir_consulta.lineEdit_10.setText(recebida[9])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum paciente foi registrada com este CPF.')
        
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Busca não realizada! informe o CPF.')

    def excluirConsulta(self):
        # menssagem do cliente
        # INFORMAÇÕES DA TELA
        cpf = self.excluir_consulta.lineEdit.text()
        menssagem =  f'excluirconsult,{cpf}'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode().split(",")
        print('recebida: ',recebida)
        if recebida[0] == '1':
            QtWidgets.QMessageBox.information(None, 'interface', 'Dado excluido')
            self.excluir_consulta.lineEdit.setText('')
            self.excluir_consulta.lineEdit_2.setText('')
            self.excluir_consulta.lineEdit_3.setText('')
            self.excluir_consulta.lineEdit_4.setText('')
            self.excluir_consulta.lineEdit_5.setText('')
            self.excluir_consulta.lineEdit_6.setText('')
            self.excluir_consulta.lineEdit_7.setText('')
            self.excluir_consulta.lineEdit_8.setText('')
            self.excluir_consulta.lineEdit_9.setText('')
            self.excluir_consulta.lineEdit_10.setText('')
        elif recebida[0] == '0':
            QtWidgets.QMessageBox.information(None, 'interface','Paciente não encontrado!')
        
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Eroo ao excluir um dado')

    def verificaTipo(self):
        cpf = self.verifica_tipo.lineEdit.text()
        if not(cpf==''):
            # menssagem do cliente
            menssagem =  f'verificartipo,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode()
            print('recebida: ',recebida)
            if recebida == '1':
                QtWidgets.QMessageBox.information(None, 'interface', 'Nova Consulta! Valor = R$:300,00')
            elif recebida == '0':
                QtWidgets.QMessageBox.information(None, 'interface', 'Retorno! Valor = Gratuito.')
            else:
                QtWidgets.QMessageBox.information(None, 'interface', 'CPF não encontrado')
        else:
            QtWidgets.QMessageBox.information(None, 'interface', 'Campo não preenchido! Imforme um CPF.')

    def buscPacMed(self):
        #menssagem do cliente
        pass
    
    
    def buscConsult(self):
        cpf = self.atualizar_consulta.lineEdit_11.text()
        if not(cpf==''):
            # menssagem do cliente
            # menssagem do usuario
            menssagem =  f'bconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            print('recebida: ',recebida)
            if recebida[0] == '1':
                self.atualizar_consulta.lineEdit_2.setText(recebida[1])
                self.atualizar_consulta.lineEdit_3.setText(recebida[2])
                self.atualizar_consulta.lineEdit_4.setText(recebida[3])
                self.atualizar_consulta.lineEdit_5.setText(recebida[4])
                self.atualizar_consulta.lineEdit_6.setText(str(recebida[5]))
                self.atualizar_consulta.lineEdit_7.setText(recebida[6])
                self.atualizar_consulta.lineEdit_8.setText(str(recebida[7]))
                self.atualizar_consulta.lineEdit_9.setText(recebida[8])
                self.atualizar_consulta.lineEdit_10.setText(recebida[9])
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", 'Nenhum paciente foi registrada com este CPF.')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Busca não realizada! informe o CPF.')

    def atualizarConsulta(self):
        cpf = self.atualizar_consulta.lineEdit_11.text()
        if not(cpf==''):
            # menssagem do cliente
            # menssagem do usuario
            menssagem =  f'atualizaconsult,{cpf}'
            cliente_socket.send(menssagem.encode())
            print('menssagem enviada')
            recebida = cliente_socket.recv(1024).decode().split(",")
            print('recebida: ',recebida)
            if recebida[0] == '1':
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta foi atualizada para o RETORNO")
            elif recebida[0] == '0':
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta foi atualizada para NOVA consulta")
            else:
                QtWidgets.QMessageBox.information(None, 'interface', f"A consulta não foi encontrada!")
           
            self.atualizar_consulta.lineEdit_11.setText('')
            self.atualizar_consulta.lineEdit_2.setText('')
            self.atualizar_consulta.lineEdit_3.setText('')
            self.atualizar_consulta.lineEdit_4.setText('')
            self.atualizar_consulta.lineEdit_5.setText('')
            self.atualizar_consulta.lineEdit_6.setText('')
            self.atualizar_consulta.lineEdit_7.setText('')
            self.atualizar_consulta.lineEdit_8.setText('')
            self.atualizar_consulta.lineEdit_9.setText('')
            self.atualizar_consulta.lineEdit_10.setText('')
        else:
            # imprime uma menssagem de erro
            QtWidgets.QMessageBox.information(None, 'interface', 'Busca não realizada! informe o CPF.')

    def excluiPacientes(self):
            item_selecionado = self.lista_pacientes.listWidget.currentItem()
            if item_selecionado is not None:
                self.lista_pacientes.listWidget.takeItem(self.lista_pacientes.listWidget.row(item_selecionado))
                menssagem = 'excluipaciente'
                cliente_socket.send(menssagem.encode())
                print('menssagem enviada')
                recebida = cliente_socket.recv(1024).decode().split(",")
                print('recebida: ',recebida)
                if recebida[0] == '1':
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "O paciente foi excluído com sucesso.")
                elif recebida[0] =='0':
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "A tabela está vazia ou não há registros para excluir.")
                else:
                    QtWidgets.QMessageBox.warning(None, "interface_grafica", "Erro ao excluir.")
            else:
                QtWidgets.QMessageBox.warning(None, "interface_grafica", "Selecione um paciente para podelo exclui-lo")
        

    def abrirTelaLoginMedico(self):
        self.QtStack.setCurrentIndex(1)
            
    def abrirTelaLoginRecepcionista(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaMedico(self):
        self.QtStack.setCurrentIndex(3)
    
    def abrirTelaRecepcionista(self):
        
        self.QtStack.setCurrentIndex(4)

    def abrirCadastroMedico(self):
        self.QtStack.setCurrentIndex(5)

    def abrirCadastroRecepcionista(self):
        self.QtStack.setCurrentIndex(6)
    
    def abrirTelaCadastros(self):
        self.QtStack.setCurrentIndex(7)
    
    def abrirCadastroRecep(self):
        self.QtStack.setCurrentIndex(8)
    
    def abrirCadastroMed(self):
        self.QtStack.setCurrentIndex(9)
    
    def abrirCadastroAdmin(self):
        self.QtStack.setCurrentIndex(10)
    
    def abrirAtendimento(self):
        self.QtStack.setCurrentIndex(11)
    
    def abrirAddGuiche(self):
        self.QtStack.setCurrentIndex(12)
    
    def abrirfinalizarAtendimento(self):  
        self.QtStack.setCurrentIndex(13)
    
    def abrirativarGuiche(self):
        self.QtStack.setCurrentIndex(14)
    
    def abrirdesativaGuiche(self):
        self.QtStack.setCurrentIndex(15)

    def abrirImpressao(self):
        self.QtStack.setCurrentIndex(16)

    def abrirImpRecep(self):
        self.QtStack.setCurrentIndex(17)
    
    def abrirImpMed(self):
        self.QtStack.setCurrentIndex(18)

    def abrirFunc(self):
        self.QtStack.setCurrentIndex(19)
    
    def abrirConsulta(self):
        self.QtStack.setCurrentIndex(20)
    
    def abrirRealizarConsult(self):
        self.QtStack.setCurrentIndex(21)
        menssagem =  f'logrecp'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode().split(",")
        print('recebida:',recebida)
        self.realizar_consulta.lineEdit_10.setText(recebida[0])
        self.realizar_consulta.comboBox.addItem("Escolha uma Opção")
        for dado in recebida[1:]:
            self.realizar_consulta.comboBox.addItem(dado)   
        self.realizar_consulta.comboBox.currentIndexChanged.connect(self.realizarConsultaAA) 

    def realizarConsultaAA(self):
        medico = self.realizar_consulta.comboBox.currentText()
        print("Opção selecionada:", medico)
        menssagem =  f'rconsult,{medico}'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode().split(",")
        print('recebida:',recebida)
        if recebida[0] == '1':
            crm = self.realizar_consulta.lineEdit_6.setText(recebida[2])
            cpf_medico = self.realizar_consulta.lineEdit_9.setText(recebida[1])
            vagas = self.realizar_consulta.lineEdit_8.setText(recebida[3])
        elif recebida[0] == '2':
            vagas = self.realizar_consulta.lineEdit_8.setText("")
            crm = self.realizar_consulta.lineEdit_6.setText(recebida[2])
            cpf_medico = self.realizar_consulta.lineEdit_9.setText(recebida[1])
            
  
       
    
        


    def abrirExcluirConsult(self):
        self.QtStack.setCurrentIndex(22)
        
    def abrirTipoConsult(self):
        self.QtStack.setCurrentIndex(23)

    def abrirImpPac(self):
        self.QtStack.setCurrentIndex(24)

    def abrirExcluirPac(self):
        self.QtStack.setCurrentIndex(25)

    def abrirExcluirGuiche(self):
        self.QtStack.setCurrentIndex(26)
    
    def abrirAtualizarCons(self):
        self.QtStack.setCurrentIndex(27)

    def abrirListaPaciente(self):
        self.QtStack.setCurrentIndex(28)

        self.lista_pacientes.listWidget.clear()
        menssagem =  f'listapacientes'
        cliente_socket.send(menssagem.encode())
        print('menssagem enviada')
        recebida = cliente_socket.recv(1024).decode().split("\n")
        print('recebida:',recebida)
    
        for item in recebida:
            self.lista_pacientes.listWidget.addItem(str(item))
        
    def abrirLoginAdmin(self):
        self.QtStack.setCurrentIndex(29)

    def sair(self): 
        """
        conexao.close()
        print('Conexão fechada com sucesso!')
        """
        cliente_socket.close()
        return exit()

    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)

    def voltarLoginMedico(self):
        self.QtStack.setCurrentIndex(1)

    def voltarLoginRecep(self):
        self.QtStack.setCurrentIndex(2)
    
    def voltarCadastros(self):
        self.QtStack.setCurrentIndex(7)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
