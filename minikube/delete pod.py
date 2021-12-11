#Delete Pod

from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_kube_config()

configuration=client.CoreV1Api()
    
namespace = 'default' 
name = 'jj4' 
    
try:
    api_response = configuration.delete_namespaced_pod(name, namespace)
    print(name, " is deleted successfully!\n")
except ApiException as e:
    print("Error in deleting the pod")
