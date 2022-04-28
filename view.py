import controller
from models.LinkedList import LinkedList

def main():

    lista_ligada = LinkedList()
    while True:
        try:
            instrucao = input().split(" ")
        except EOFError:
            return 

        #Registar País no Inicio
        if instrucao[0] == "RPI":
            RPI(lista_ligada, instrucao[1])

        #Registar País no Fim
        elif instrucao[0] == "RPF":
            RPF(lista_ligada, instrucao[1])

        #Registar País Depois de outro Elemento
        elif instrucao[0] == "RPDE":
            RPDE(lista_ligada, instrucao[1], instrucao[2])

        #Registar País Antes de outro Elemento
        elif instrucao[0] == "RPAE":
            RPAE(lista_ligada, instrucao[1], instrucao[2])

        #Registar País Índice Introduzido
        elif instrucao[0] == "RPII":
            RPII(lista_ligada, instrucao[1], instrucao[2])

        #Verificar Número de Elementos
        elif instrucao[0] == "VNE":
            VNE(lista_ligada)

        #Verificar País
        elif instrucao[0] == "VP":
            VP(lista_ligada, instrucao[1])

        #Eliminar Primeiro Elemento
        elif instrucao[0] == "EPE":
            EPE(lista_ligada)

        #Eliminar Último Elemento
        elif instrucao[0] == "EUE":
            EUE(lista_ligada)

        #Eliminar Páis
        elif instrucao[0] == "EP":
            EP(lista_ligada, instrucao[1])


def RPI(lista_ligada, pais):
    controller.registar_pais_inicio(lista_ligada, pais)
    return lista_ligada.traverse_list()



def RPF(lista_ligada, pais):
    controller.registar_pais_fim(lista_ligada, pais)
    return lista_ligada.traverse_list()



def RPDE(lista_ligada, pais_novo, pais_antigo):
    controller.registar_pais_depois_elemento(lista_ligada, pais_antigo, pais_novo)
    return lista_ligada.traverse_list()



def RPAE(lista_ligada, pais_novo, pais_antigo):
    controller.registar_pais_antes_elemento(lista_ligada,pais_antigo, pais_novo)
    return lista_ligada.traverse_list()



def RPII(lista_ligada, pais, indice):
    controller.registar_pais_indice_introduzido(lista_ligada, pais, indice)
    return lista_ligada.traverse_list()



def VNE(lista_ligada):
    print(f"O número de elementos são {controller.verificar_numero_elementos(lista_ligada)}.")



def VP(lista_ligada, pais):

    resultado = controller.verificar_pais(lista_ligada, pais)

    if resultado == True:
        print(f"O país {pais} encontra-se na lista.")
    else:
        print(f"O país {pais} não se encontra na lista.")



def EPE(lista_ligada):  
    print(f"O país {controller.eliminar_primeiro_elemento(lista_ligada)} foi eliminado da lista.")



def EUE(lista_ligada):
    print(f"O país {controller.eliminar_ultimo_elemento(lista_ligada)} foi eliminado da lista.")


def EP(lista_ligada, pais):
    
    resultado = controller.eliminar_pais(lista_ligada, pais)

    if resultado == True:
        print(f"O país {pais} foi eliminado da lista.")
    else:
        print(f"O país {pais} não se encontra na lista.")
