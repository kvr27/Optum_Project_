# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

grp_df = read_bronze_csv("group")

# COMMAND ----------

df_row_columns(grp_df)

# COMMAND ----------

check_missing_values(grp_df,grp_df.columns)

# COMMAND ----------

check_string_as_nan(grp_df)

# COMMAND ----------

check_duplicates(grp_df,grp_df.columns)

# COMMAND ----------

display(grp_df)  #action

# COMMAND ----------

write2silver(grp_df,"Group_S.csv")