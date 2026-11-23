import os
from google.cloud import bigquery

# Set proxy
os.environ['HTTPS_PROXY'] = 'http://clientproxy.nat.bt.com:8080'

print("=== BigQuery Datasets in or-odiaa-aif-exp-prod ===\n")

try:
    client = bigquery.Client(project='or-odiaa-aif-exp-prod')
    datasets = list(client.list_datasets())
    
    print(f"Found {len(datasets)} datasets:\n")
    
    for i, dataset in enumerate(datasets, 1):
        print(f"{i:2d}. {dataset.dataset_id}")
        
except Exception as e:
    print(f"Error: {e}")