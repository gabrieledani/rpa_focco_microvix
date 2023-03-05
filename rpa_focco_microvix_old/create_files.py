import logging
import cx_Oracle
from datetime import datetime
import os

diretorio = os.getcwd()

def database_connect():
    """starts oracle client and returns connection object"""
    try:
        oracle_lib = file = os.path.join(diretorio,"instantclient_21_3")
        cx_Oracle.init_oracle_client(lib_dir=oracle_lib)
    except:
        pass
    
    #[ORACLE]
    ip = 'oracle'
    #port = '1521'
    sid = 'f3ipro'
    user = 'FOCCO3i'
    password = 'serv17'
    
    connection = cx_Oracle.connect(
        user,
        password,
        f'{ip}/{sid}')

    return connection

def import_query(filename):
    """opens sql file and returns a list with all queries inside"""
    file = open(filename)
    full_sql = file.read()
    sql_commands = full_sql.strip()
    return sql_commands


def select_data(cursor, sql_file, empr_id, par_almox):
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Obtendo dados do Banco Oracle")

    sql_commands = import_query(sql_file)
    
    sql_commands = sql_commands.replace('PI_EMPR_ID',empr_id)
    sql_commands = sql_commands.replace('PI_COD_ALMOX',par_almox)

    cursor.execute(sql_commands)
    query_result = cursor.fetchall()
    
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Dados obtidos com sucesso")
    return query_result


def save_items_file(result_query,emp,almox):
    stock_file = open('ESTOQUE_'+emp+'_'+almox+'.CSV','w')
    
    for row in result_query:
        cod_barra = row[0].strip()
        #print(cod_barra)
        estq = row[1].replace(',','.')
        #print(estq)
        stock_file.write(cod_barra+';'+estq+'\n')
        
    stock_file.close()
    return stock_file


def find_param(cursor,empresa,type):
    if type == 'EMPRESA_PADRAO':
        sql_commands = "SELECT FOCCO3I_UTIL.RETORNA_PARAMETRO('INT_MICROVIX', 'EMPRESA_PADRAO', NULL, NULL) FROM DUAL"
    else:
        sql_commands = "SELECT FOCCO3I_UTIL.RETORNA_PARAMETRO('INT_MICROVIX', 'ALMOX_PADRAO', "+empresa+", NULL) FROM DUAL"
    
    #print(sql_commands)
    
    cursor.execute(sql_commands)
    query_result = cursor.fetchall()

    return query_result[0][0]

   
def execute(empresa):
    # Logging configuration
    logging.basicConfig(filename='application.log',level=logging.INFO,format='%(asctime)s - %(message)s')
    
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Iniciando conexao com o banco Oracle")
    connection = database_connect()

    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Conexao estabelecida")
    cur = connection.cursor()
    
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Iniciando sincronizacao de dados de estoque")
    #parametro de almox
    param_type = 'EMPRESA_PADRAO'
    emp = find_param(cur,'NULL',param_type)

    param_type = 'ALMOX_PADRAO'
    almox = find_param(cur,emp,param_type)

    result = select_data(cur, 'produtos.sql', empresa, almox)
    
    file = save_items_file(result, empresa, almox)
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Sincronizacao de estoque completa")
    
    #logging.info(datetime.now().strftime("%H:%M:%S - ") + "Processo para setar estoque completo")
    connection.close()
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Conexao com o banco Oracle encerrada")
    try:
        pass
    except Exception as exception:
        logging.info(datetime.now().strftime("%H:%M:%S - ") + f'{exception}, por favor reinicie a aplicacao.')
        logging.info(datetime.now().strftime("%H:%M:%S - ") + f'{type(exception)}')
    
    return file



