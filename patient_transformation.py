# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

pat_df = read_bronze_csv("Patient_records")

# COMMAND ----------

df_row_columns(pat_df)

# COMMAND ----------

check_missing_values(pat_df,pat_df.columns)

# COMMAND ----------

check_string_as_nan(pat_df)

# COMMAND ----------

check_duplicates(pat_df,pat_df.columns)

# COMMAND ----------

display(pat_df)  #action

# COMMAND ----------

pat_df = pat_df.fillna({'patient_name':"Visitor/NA"})
pat_df = pat_df.drop('patient_phone')
pat_df = pat_df.withColumn("patient_age", (months_between(current_date(), pat_df.patient_birth_date)/12).cast("integer"))
pat_df = pat_df.drop('patient_birth_date')

# COMMAND ----------

display(pat_df.limit(16))

# COMMAND ----------

write2silver(pat_df,"Patient_S.csv")