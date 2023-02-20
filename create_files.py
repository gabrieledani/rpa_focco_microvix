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

def find_param(cursor, par_emp):
    #par_emp = 91
    sql_commands = "SELECT FOCCO3I_UTIL.RETORNA_PARAMETRO('INT_MICROVIX', 'ALMOX_PADRAO', "+par_emp+", NULL) FROM DUAL"
    cursor.execute(sql_commands)
    query_result = cursor.fetchall()
    return query_result[0][0]

def import_query(filename):
    """opens sql file and returns a list with all queries inside"""
    file = open(filename)
    full_sql = file.read()
    sql_commands = full_sql.strip()
    return sql_commands

def select_data(cursor, sql_file, par_emp, par_almox):
    #par_emp = 91
    #par_almox = 070
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Obtendo dados do Banco Oracle")

    sql_commands = import_query(sql_file)
    
    sql_commands = sql_commands.replace('PI_EMPR_ID',par_emp)
    sql_commands = sql_commands.replace('PI_COD_ALMOX',par_almox)

    cursor.execute(sql_commands)
    query_result = cursor.fetchall()
    
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Dados obtidos com sucesso")
    return query_result

def save_items_file(result_query,par_emp,par_almox):
    #par_emp = 91
    #par_almox = 070
    stock_file = open('ESTOQUE_'+par_emp+'_'+par_almox+'.CSV','w')
    
    for row in result_query:
        cod_barra = row[0].strip()
        estq = row[1].replace(',','.')
        stock_file.write(cod_barra+';'+estq+'\n')
        
    stock_file.close()
    return stock_file

   
def execute(empresa):
    # Logging configuration
    logging.basicConfig(filename='application.log',level=logging.INFO,format='%(asctime)s - %(message)s')

    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Gerando aquivo de estoque da Empresa:"+empresa)
    
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Iniciando conexao com o banco Oracle")
    connection = database_connect()

    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Conexao estabelecida")
    cur = connection.cursor()
    
    #parametro de almox
    almox = find_param(cur,empresa)
    
    result = select_data(cur, 'produtos.sql', empresa, almox)
    
    file = save_items_file(result, empresa, almox)
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Arquivo estoque gerado")
    
    connection.close()
    logging.info(datetime.now().strftime("%H:%M:%S - ") + "Conexao com o banco Oracle encerrada")
    
    return file