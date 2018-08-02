import requests
import pandas as pd
import os
import ast

# CLUSTERS

def get_cluster_server_dict():
    csd = {
        'DHDP001': 'OMHQ1943',
        'BHDP001': 'OMSDP137FB',
        'PHBA001': 'OMHQP11804',
        'PHDP001': 'OMHQP125DD',
        'PHDP002': 'OMHQP138C9',
        'XHBA001': 'OMSDP11A80',
        'XHDP001': 'OMDXP125F5',
        'XHDP002': 'OMSDP130F4'
    }
    return csd

def get_server(cluster):
    csd = get_cluster_server_dict()
    if cluster in csd:
        return csd[cluster]
    return 'Invalid'

def get_data(server):
    url = 'http://' + server + '.uprr.com:50070/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo'
    data = requests.get(url).json()
    return data

def get_total(data):
    return data['Total']

def is_safe_mode(data):
    return data['Safemode'] == 'Yes'

def get_percent_used(data):
    return data['PercentUsed']

def get_percent_remaining(data):
    return data['PercentRemaining']

def get_num_missing_blocks(data):
    return data['NumberOfMissingBlocks']

def has_dead_nodes(data):
    deadNodes = data['DeadNodes']
    return deadNodes != '{}'

def has_decom_nodes(data):
    decomNodes = data['DecomNodes']
    return decomNodes != '{}'

def has_corrupt_files(data):
    corruptFiles = data['CorruptFiles']
    return corruptFiles != '[]'

def get_nn_started(data):
	return data['NNStarted']

def get_cluster_info(cluster):
    server = get_server(cluster)
    data = get_data(server)
    data_index = data['beans'][0]

    total = get_total(data_index)
    safe_mode = is_safe_mode(data_index)
    percent_used = get_percent_used(data_index)
    percent_remaining = get_percent_remaining(data_index)
    num_missing_blocks = get_num_missing_blocks(data_index)
    dead_nodes = has_dead_nodes(data_index)
    decom_nodes = has_decom_nodes(data_index)
    corrupt_files = has_corrupt_files(data_index)
    nn_started = get_nn_started(data_index)

    cluster_info = {
        'server': server,
        'total': total,
        'safe_mode': safe_mode,
        'percent_used': percent_used,
        'percent_remaining': percent_remaining,
        'num_missing_blocks': num_missing_blocks,
        'dead_nodes': dead_nodes,
        'decom_nodes': decom_nodes,
        'corrupt_files': corrupt_files,
        'nn_started': nn_started
    }
    return cluster_info

# DATABASES

def convert_db_csv():
    # Get path
    folder = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(folder, 'db.csv')

    # Create a pandas data frame
    df = pd.read_csv(db_file, header = None)
    df.columns = ['DB_ID', 'DESC', "DB_LOCATION_URI", 'NAME', 'OWNER_TYPE', 'OWNER_NAME']
    return df

def get_database_list():
    df = convert_db_csv()
    return df.NAME.tolist()

def get_database_info(database):
    df = convert_db_csv()
    pd.set_option('display.max_columns', None)

    info = df.loc[df['NAME'] == database]

    db_id = info['DB_ID'].item()
    db_desc = info['DESC'].item()
    db_owner = info['OWNER_NAME'].item()

    return 'ID: ' + str(db_id) + '\nDESC: ' + str(db_desc) + '\nOWNER: ' + str(db_owner)