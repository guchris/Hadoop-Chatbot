from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import data.verify as verify
import data.data_retrieval as data_retrieval

class ActionGetRequest(Action):

    def name(self):
        return 'action_get_request'
    
    def run(self, dispatcher, tracker, domain):
        # Append failed user request to end of 'requests.txt'
        request = str(tracker.get_slot('request'))
        with open('requests.txt', 'a') as requests:
            requests.write(request + '\n')
        return []

class ActionGetHadoopProductionCapacity(Action):

    def name(self):
        return 'action_get_hadoop_production_capacity'
    
    def run(self, dispatcher, tracker, domain):
        csd = data_retrieval.get_cluster_server_dict()
        total_production_capacity = 0
        for key in csd:
            cluster_info = data_retrieval.get_cluster_info(key)
            total_production_capacity += int(cluster_info['total'])
        dispatcher.utter_message('Hadoop Production Capacity: ' + str(total_production_capacity))
        return []


class ActionGetClusterStatuses(Action):

    def name(self):
        return 'action_get_cluster_statuses'
    
    def run(self, dispatcher, tracker, domain):
        # Check healthiness of all clusters
        csd = data_retrieval.get_cluster_server_dict()
        safe_mode_clusters = []
        warning_clusters = []
        for key in csd:
            cluster_info = data_retrieval.get_cluster_info(key)
            if cluster_info['safe_mode']:
                safe_mode_clusters.append(key)
            if (cluster_info['percent_used'] >= 70.0 or
                cluster_info['num_missing_blocks'] > 0 or
                cluster_info['dead_nodes'] or
                cluster_info['decom_nodes'] or
                cluster_info['corrupt_files']):
                warning_clusters.append(key)
        
        # Health responses
        if not safe_mode_clusters:
            dispatcher.utter_message('All clusters are healthy.')
        else:
            if len(safe_mode_clusters) == 1:
                dispatcher.utter_message('1 cluster is unhealthy: ' + safe_mode_clusters[0])
            else:
                safe_mode_clusters_str = ''
                for cluster in safe_mode_clusters:
                    if cluster == safe_mode_clusters[-1]:
                        safe_mode_clusters_str += cluster
                    else:
                        safe_mode_clusters_str += cluster + ', '
                dispatcher.utter_message(str(len(safe_mode_clusters)) + ' clusters are unhealthy: ' + safe_mode_clusters_str)
        
        # Warning responses
        if len(warning_clusters) == 1:
            dispatcher.utter_message('1 cluster has warnings: ' + warning_clusters[0])
        else:
            warning_clusters_str = ''
            for cluster in warning_clusters:
                if cluster == warning_clusters[-1]:
                    warning_clusters_str += cluster
                else:
                    warning_clusters_str += cluster + ', '
            dispatcher.utter_message(str(len(warning_clusters)) + ' clusters have warnings: ' + warning_clusters_str)
        return []

class ActionGetEmptiestCluster(Action):
    
    def name(self):
        return 'action_get_emptiest_cluster'
    
    def run(self, dispatcher, tracker, domain):
        # Find cluster with the most space available
        csd = data_retrieval.get_cluster_server_dict()
        emptiest_cluster = ["tmp", -1.0]
        for key in csd:
            cluster_info = data_retrieval.get_cluster_info(key)
            if cluster_info['percent_remaining'] > emptiest_cluster[1]:
                emptiest_cluster = [str(key), cluster_info['percent_remaining']]
        dispatcher.utter_message(emptiest_cluster[0] + ' has the most space available with ' + str(emptiest_cluster[1]) + '% free.')
        return []

class ActionGetFullestCluster(Action):

    def name(self):
        return 'action_get_fullest_cluster'
    
    def run(self, dispatcher, tracker, domain):
        # Find cluster with the least space available
        csd = data_retrieval.get_cluster_server_dict()
        fullest_cluster = ["tmp", -1.0]
        for key in csd:
            cluster_info = data_retrieval.get_cluster_info(key)
            if cluster_info['percent_used'] > fullest_cluster[1]:
                fullest_cluster = [str(key), cluster_info['percent_used']]
        dispatcher.utter_message(fullest_cluster[0] + ' has the least space available with ' + str(fullest_cluster[1]) + '% used.')
        return []

class ActionGetClusterStatus(Action):

    def name(self):
        return 'action_get_cluster_status'
    
    def run(self, dispatcher, tracker, domain):
        # Verify cluster
        cluster = str(tracker.get_slot('cluster')).upper()
        if not verify.is_cluster(cluster):
            return [SlotSet('is_valid', False)]
        else:
            # Check cluster stats
            cluster_info = data_retrieval.get_cluster_info(cluster)
            if cluster_info['safe_mode']:
                dispatcher.utter_message(cluster + ' is unhealthy.')
                dispatcher.utter_message('ERROR: Cluster is in safe mode!')
            else:
                dispatcher.utter_message(cluster + ' is healthy.')
                if cluster_info['percent_used'] >= 70:
                    dispatcher.utter_message('WARNING: Storage usage of ' + str(cluster_info['percent_used']) + '% is above healthy levels.')
                if cluster_info['num_missing_blocks'] > 0:
                    dispatcher.utter_message('WARNING: There are ' + str(cluster_info['num_missing_blocks']) + ' missing blocks.')
                if cluster_info['dead_nodes']:
                    dispatcher.utter_message('WARNING: There is at least 1 dead node.')
                if cluster_info['decom_nodes']:
                    dispatcher.utter_message('WARNING: There is at least 1 decom node.')
                if cluster_info['corrupt_files']:
                    dispatcher.utter_message('WARNING: There is at least 1 corrupt file.')
            return [SlotSet('is_valid', True)]

class ActionGetClusterNNStarted(Action):
    
    def name(self):
        return 'action_get_cluster_nn_started'
    
    def run(self, dispatcher, tracker, domain):
        # Verify cluster
        cluster = str(tracker.get_slot('cluster')).upper()
        if not verify.is_cluster(cluster):
            return [SlotSet('is_valid', False)]
        
        # Utter cluster nn_started
        cluster_info = data_retrieval.get_cluster_info(cluster)
        dispatcher.utter_message(cluster + '\'s NameNode started on ' + str(cluster_info['nn_started']) + '.')
        return [SlotSet('is_valid', True)]

class ActionGetClusterURL(Action):
    
    def name(self):
        return 'action_get_cluster_url'
    
    def run(self, dispatcher, tracker, domain):
        # Verify cluster
        cluster = str(tracker.get_slot('cluster')).upper()
        if not verify.is_cluster(cluster):
            return [SlotSet('is_valid', False)]
        
        # Utter cluster url
        server = data_retrieval.get_server(cluster)
        dispatcher.utter_message('http://' + server + '.uprr.com:50070/jmx?qry=Hadoop:service=NameNode,name=NameNodeInfo')
        return [SlotSet('is_valid', True)]

class ActionGetDatabases(Action):

    def name(self):
        return 'action_get_databases'
    
    def run(self, dispatcher, tracker, domain):
        # Retrieve all databases
        dbl = data_retrieval.get_database_list()
        count = str(len(dbl))

        # Utter a few databases
        dispatcher.utter_message('Here are the first 10 databases (' + count + ' total):')
        dispatcher.utter_message(str(dbl[0:10]))
        return []

class ActionGetDatabaseSpecifics(Action):

    def name(self):
        return 'action_get_database_specifics'
    
    def run(self, dispatcher, tracker, domain):
        # Verify database
        db = str(tracker.get_slot('database')).lower()
        if not verify.is_database(db):
            return [SlotSet('is_valid', False)]
        
        # Utter database details
        dispatcher.utter_message('Details for the ' + str(db) + ' database:')
        db_info = data_retrieval.get_database_info(db)
        dispatcher.utter_message(db_info)
        return [SlotSet('is_valid', True)]