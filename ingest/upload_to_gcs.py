import os
import pandas as pd
from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    
    """
    Uploads a file to a GCS bucket.

    :param bucket_name: Name of the GCS bucket.
    :param source_file_path: Path to the file to upload.
    :param destination_blob_name: The name of the blob (file) in the bucket.
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(source_file_path)
    print(f"File {source_file_path} uploaded to {destination_blob_name}.")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'strategic-grove-441411-g1-b3415830bd10.json'

bucket = "sales_analytics"    

file_name = "raw/orders.csv"
upload_to_gcs(bucket,file_name,file_name)

file_name = "raw/products.csv"
upload_to_gcs(bucket,file_name,file_name)

file_name = "raw/customers.csv"
upload_to_gcs(bucket,file_name,file_name)