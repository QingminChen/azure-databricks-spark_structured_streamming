# Databricks notebook source
mount_point_path = dbutils.widgets.text('mount_point_path','/mnt/datalake')
file_system = dbutils.widgets.text('file_system','datalake')
account_name = dbutils.widgets.text('account_name','teststorage2222')

# COMMAND ----------

client_id = dbutils.secrets.get('test_scope','ApplicationClientID') # key is the scope name which needs to point to the KV enpoint, value is the secret name which was imported with the specific KV enpoint name
# # dbutils.widgets.text('file_system','datalake')
# # dbutils.widgets.text('account_name','teststorage2222')

mount_point_path = dbutils.widgets.text('mount_point_path','/mnt/datalake')
file_system = dbutils.widgets.text('file_system','datalake')
account_name = dbutils.widgets.text('account_name','teststorage2222')

tenant_str = 'https://login.microsoftonline.com/' + '2890298d-6798-4ee8-8e84-320d2c1268cb' + '/oauth2/token'
configs = {
'fs.azure.account.auth.type':'OAuth',
'fs.azure.account.oauth.provider.type':'org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider',
# 'fs.azure.account.oauth2.client.id':'af123379-59f7-45b0-a273-d940a370c092',
'fs.azure.account.oauth2.client.id':client_id,
'fs.azure.account.oauth2.client.secret':dbutils.secrets.get(scope='test_scope',key='testkvsecret2'),
#     'fs.azure.account.oauth2.client.secret':'GW68Q~qyCZp_o02LzF2MjGiLvDTxO_-Q2prandAZ',
'fs.azure.account.oauth2.client.endpoint':tenant_str
}

dbutils.fs.mount(
source = 'abfss://datalake@teststorage2222.dfs.core.windows.net',
mount_point = '/mnt/filefolder4',
extra_configs = configs 
)

# COMMAND ----------

dbutils.fs.ls('/mnt/')

# COMMAND ----------

# spark.read.load("abfss://datalake@teststorage2222.dfs.core.windows.net/N3-kaitou.pdf")

# dbutils.fs.ls("abfss://datalake@teststorage2222.dfs.core.windows.net/")





service_credential = dbutils.secrets.get(scope="test_scope",key="testkvsecret2")

spark.conf.set("fs.azure.account.auth.type.teststorage2222.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.teststorage2222.dfs.core.windows.net","org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.teststorage2222.dfs.core.windows.net", "af123379-59f7-45b0-a273-d940a370c092")
spark.conf.set("fs.azure.account.oauth2.client.secret.teststorage2222.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.teststorage2222.dfs.core.windows.net", "https://login.microsoftonline.com/2890298d-6798-4ee8-8e84-320d2c1268cb/oauth2/token")
spark.conf.set("spark.databricks.delta.formatCheck.enabled","false")

spark.read.load("abfss://datalake@teststorage2222.dfs.core.windows.net/test/stream/test_delta_tb.delta") # Here we read the delta format data directly from the container not through the mount local storage which is not recommended

## need to figure out what the delta data as offline file 's format should be looking like

# COMMAND ----------

# abc = dbutils.secrets.get("test_scope","testkvsecret2")
# print(abc)
