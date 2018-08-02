import data.data_retrieval as data_retrieval

def is_cluster(cluster):
    if cluster is not None:
        csd = data_retrieval.get_cluster_server_dict()
        if cluster not in csd:
            return False
        return True
    return False

def is_database(database):
    if database is not None:
        dbl = data_retrieval.get_database_list()
        if database not in dbl:
            return False
        return True
    return False