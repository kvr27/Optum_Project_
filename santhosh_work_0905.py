# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"

# COMMAND ----------

configs = {
    'fs.azure.account.key.optumsadls.blob.core.windows.net': dbutils.secrets.get(scope="optumscope", key="adlsacesskey")
}

# COMMAND ----------

display(dbutils.secrets.listScopes())

# COMMAND ----------

display(dbutils.secrets.list("optumscope"))

# COMMAND ----------

dbutils.fs.unmount("/mnt/optumbrzpt/")

# COMMAND ----------

dbutils.fs.mount(
source = "wasbs://optum@optumsadls.blob.core.windows.net/medallion/bronze",
mount_point = '/mnt/optumbrzpt/',
extra_configs = configs
)

# COMMAND ----------

dbutils.fs.mount(
source = "wasbs://optum@optumsadls.blob.core.windows.net/medallion/silver",
mount_point = '/mnt/optumslvpt/',
extra_configs = configs
)

# COMMAND ----------

dbutils.fs.mount(
source = "wasbs://optum@optumsadls.blob.core.windows.net/medallion/gold",
mount_point = '/mnt/optumgldpt/',
extra_configs = configs
)

# COMMAND ----------

display(dbutils.fs.ls("/mnt/optumbrzpt/"))

# COMMAND ----------

list_bronze_files()

# COMMAND ----------



# COMMAND ----------

list_silver_files()

# COMMAND ----------

list_gold_files()

# COMMAND ----------

hos = read_bronze_csv("Hospital")

# COMMAND ----------

hos.count(), len(hos.columns)

# COMMAND ----------

display(hos.limit(5))

# COMMAND ----------

dis = read_bronze_csv("disease")

# COMMAND ----------

display(dis.limit(5))

# COMMAND ----------

clms = read_bronze_json("Claims")

# COMMAND ----------

sample_data(clms)

# COMMAND ----------

sample_data(dis)

# COMMAND ----------

install_libraries()

# COMMAND ----------

write2sqldatabase(dis, "disease_tb")

# COMMAND ----------

write2sqldatabase(hos, "hospital_tb")

# COMMAND ----------

display(write2silver(hos,"Hospital_S.csv"))

# COMMAND ----------

display(write2gold(hos,"Hospital_G.csv"))

# COMMAND ----------

display(write2silver(dis,"Disease_S.csv"))