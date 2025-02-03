from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from django.conf import settings


def appwrite_client():
    client = Client()
    client.set_endpoint(settings.APPWRITE_ENDPOINT)
    client.set_project(settings.APPWRITE_PROJECT_ID)
    client.set_key(settings.APPWRITE_API_KEY)
            
    # Create user document in Appwrite
    databases = Databases(client)
    document_id = ID.unique()


    return databases, document_id