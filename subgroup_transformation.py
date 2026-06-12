# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

subgrp_df = read_bronze_csv("subgroup")

# COMMAND ----------

df_row_columns(subgrp_df)

# COMMAND ----------

check_missing_values(subgrp_df,subgrp_df.columns)

# COMMAND ----------

check_string_as_nan(subgrp_df)

# COMMAND ----------

check_duplicates(subgrp_df,subgrp_df.columns)

# COMMAND ----------

display(subgrp_df)  #action

# COMMAND ----------

subgrp_df = subgrp_df.withColumn("subgrp_id", split(col("subgrp_id"),","))

# COMMAND ----------

display(subgrp_df)

# COMMAND ----------

subgrp_df = subgrp_df.withColumn("subgrp_id", explode(col("subgrp_id")))

# COMMAND ----------

display(subgrp_df)

# COMMAND ----------

write2silver(subgrp_df,"SubGroup_S.csv")