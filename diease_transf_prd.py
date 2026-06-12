# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

dis_df = read_bronze_csv("disease")

# COMMAND ----------

dis_df.select("*").filter(col("disease_name") == 'Flu').show(5)

# COMMAND ----------

dis_df.select("*").filter(col("disease_name").like("%cancer%")).show(5)

# COMMAND ----------

write2silver(dis_df,"disease_S.csv")