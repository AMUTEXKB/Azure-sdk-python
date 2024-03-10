from azure.identity import DefaultAzureCredential
import os
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters
from azure.mgmt.resource import ResourceManagementClient
# Get Azure subscription ID from environment variable
subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
if not subscription_id:
    raise ValueError("AZURE_SUBSCRIPTION_ID environment variable is not set.")

# Authenticate using DefaultAzureCredential
credentials = DefaultAzureCredential()
# Initialize ResourceManagementClient for managing resource groups
resource_client = ResourceManagementClient(credentials, subscription_id)

# Initialize StorageManagementClient
storage_client = StorageManagementClient(credentials, subscription_id)

# Define resource group and storage account parameters
resource_group_name = "amutexblob2"
storage_account_name = "amutex1234"
location = "westus"

# Create or update resource group
resource_group_params = {"location": location}
rg_result = resource_client.resource_groups.create_or_update(resource_group_name, resource_group_params)
print(f"Provisioned resource group {rg_result.name}")

# Create storage account
storage_account_params = StorageAccountCreateParameters(
    sku={"name": "Standard_LRS"},  # Adjust SKU as needed
    kind="StorageV2",
    location=location
)

storage_account = storage_client.storage_accounts.begin_create(resource_group_name, storage_account_name, storage_account_params)
print(f"Provisioned storage account {storage_account.result}")
