from azure.storage.blob import BlobServiceClient
import os

container_name = "audios"
connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]

def upload_audio_to_blob(filepath: str) -> str:
    blob_service = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service.get_blob_client(container=container_name, blob=os.path.basename(filepath))
    with open(filepath, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    return blob_client.url
