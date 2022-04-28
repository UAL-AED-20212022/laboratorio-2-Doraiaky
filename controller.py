


#Registar País no Inicio
def registar_pais_inicio(lista_ligada, pais):
    lista_ligada.insert_at_start(pais)
    return lista_ligada


#Registar País no Fim
def registar_pais_fim(lista_ligada, pais):
    lista_ligada.insert_at_end(pais)
    return lista_ligada


#Registar País Depois de outro Elemento
def registar_pais_depois_elemento(lista_ligada, pais_antigo, pais_novo):
    lista_ligada.insert_after_item(pais_antigo, pais_novo)
    return lista_ligada


#Registar País Antes de outro Elemento
def registar_pais_antes_elemento(lista_ligada, pais_antigo, pais_novo):
    lista_ligada.insert_before_item(pais_antigo, pais_novo)
    return lista_ligada


#Registar País Índice Introduzido
def registar_pais_indice_introduzido(lista_ligada, pais, indice):
    lista_ligada.insert_at_index(int(indice), pais)
    return lista_ligada


#Verificar Número de Elementos
def verificar_numero_elementos(lista_ligada):
    return lista_ligada.get_count()


#Verificar País
def verificar_pais(lista_ligada, pais):
    resultado = lista_ligada.search_item(pais)
    return resultado


#Eliminar Primeiro Elemento
def eliminar_primeiro_elemento(lista_ligada):
    primeiro_elemento = lista_ligada.start_node.item
    lista_ligada.delete_at_start()
    return primeiro_elemento


#Eliminar Último Elemento
def eliminar_ultimo_elemento(lista_ligada):
    ultimo_elemento = lista_ligada.get_last_node()
    lista_ligada.delete_at_end()
    return ultimo_elemento


#Eliminar Páis
def eliminar_pais(lista_ligada, pais):
    if lista_ligada.search_item(pais) == True:
        lista_ligada.delete_element_by_value(pais)
        return True
    else:
        return False