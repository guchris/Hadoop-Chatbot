## default
* default{"request": "temp"}
    - utter_default
    - action_get_request

## help
* help
    - utter_help

## greet
* greet
    - utter_greet

## bye
* bye
    - utter_bye
    - action_restart

<!-- CLUSTERS -->

## hadoop_production_capacity_request
* hadoop_production_capacity_request
    - action_get_hadoop_production_capacity

## cluster_statuses_request
* cluster_statuses_request
    - action_get_cluster_statuses

## cluster_emptiest_request
* cluster_emptiest_request
    - action_get_emptiest_cluster

## cluster_fullest_request
* cluster_fullest_request
    - action_get_fullest_cluster

<!-- status -->
## cluster_status_request 1
* cluster_status_request
    - utter_ask_cluster
* cluster_status_inform{"cluster": "phdp001"}
    - slot{"cluster": "phdp001"}
    - action_get_cluster_status
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## cluster_status_request 2
* cluster_status_request
    - utter_ask_cluster
* cluster_status_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_status
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

## cluster_status_inform 1
* cluster_status_inform{"cluster": "phdp001"}
    - slot{"cluster": "phdp001"}
    - action_get_cluster_status
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## cluster_status_inform 2
* cluster_status_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_status
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

<!-- nn started -->
## cluster_nn_started_request 1
* cluster_nn_started_request
    - utter_ask_cluster
* cluster_status_inform{"cluster": "phdp001"}
    - slot{"cluster": "phdp001"}
    - action_get_cluster_nn_started
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## cluster_nn_started_request 2
* cluster_nn_started_request
    - utter_ask_cluster
* cluster_status_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_nn_started
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

## cluster_nn_started_inform 1
* cluster_nn_started_inform{"cluster": "phdp001"}
    - slot{"cluster": "phdp001"}
    - action_get_cluster_nn_started
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## cluster_nn_started_inform 2
* cluster_nn_started_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_nn_started
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

<!-- url -->
## cluster_url_request 1
* cluster_url_request
    - utter_ask_cluster
* cluster_status_inform{"cluster": "phdp001"}
    - slot{"cluster": "phdp001"}
    - action_get_cluster_url
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## cluster_url_request 2
* cluster_url_request
    - utter_ask_cluster
* cluster_status_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_url
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

## cluster_url_inform 1
* cluster_url_inform{"cluster": "phdp001"}
    - slot{"cluster": "phdp001"}
    - action_get_cluster_url
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## cluster_url_inform 2
* cluster_url_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_url
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

<!-- DATABASES -->

## databases_request
* databases_request
    - action_get_databases
    - utter_db_prompt

<!-- specifics -->
## database_specifics_request 1
* database_specifics_request
    - utter_ask_database
* database_specifics_inform{"database": "prj_web_logs"}
    - slot{"database": "prj_web_logs"}
    - action_get_database_specifics
    - slot{"is_valid": true}
    - action_restart

## database_specifics_request 2
* database_specifics_request
    - utter_ask_database
* database_specifics_inform{"database": null}
    - slot{"database": null}
    - action_get_database_specifics
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

## database_specifics_inform 1
* database_specifics_inform{"database": "prj_dag"}
    - slot{"database": "prj_dag"}
    - action_get_database_specifics
    - slot{"is_valid": true}
    - action_restart

## database_specifics_inform 2
* database_specifics_inform{"database": null}
    - slot{"database": null}
    - action_get_database_specifics
    - slot{"is_valid": false}
    - utter_invalid
    - action_restart

<!-- INTERACTIVE LEARNING STORIES -->
## Generated Story -9070840857493355627
* greet
    - utter_greet
* cluster_status_inform{"cluster": "xhdp001"}
    - slot{"cluster": "xhdp001"}
    - action_get_cluster_status
    - slot{"is_valid": true}
    - utter_ask_cluster_specifics

## Generated Story 1534867797787841517
* greet
    - utter_greet
* cluster_status_inform{"cluster": null}
    - slot{"cluster": null}
    - action_get_cluster_status 
    - slot{"is_valid": false}
    - utter_invalid

## Generated Story 5102068580610453984
* database_specifics_request
    - utter_ask_database
* database_specifics_inform{"database": "usr_iots193"}
    - slot{"database": "usr_iots193"}
    - action_get_database_specifics
    - slot{"is_valid": true}
