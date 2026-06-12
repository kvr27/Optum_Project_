# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

sub_df = read_bronze_csv("subscriber")

# COMMAND ----------

df_row_columns(sub_df)

# COMMAND ----------

check_missing_values(sub_df,sub_df.columns)

# COMMAND ----------

display(sub_df.limit(10))

# COMMAND ----------

check_string_as_nan(sub_df)

# COMMAND ----------

check_duplicates(sub_df,sub_df.columns)

# COMMAND ----------

sub_df = sub_df.fillna({"first_name":"Visitor/NA", "Elig_ind":"N"})
sub_df = sub_df.drop("Phone")
sub_df = sub_df.withColumn("Subsriber_age", (months_between(current_date(), col("Birth_date"))/12).cast("integer"))
sub_df = sub_df.drop("Birth_date")

# COMMAND ----------

display(sub_df.limit(10))
sub_df = sub_df.filter(col("Subsriber_age") >= 0)
display(sub_df)

# COMMAND ----------

display(sub_df.select("*").filter(col("Subgrp_id").isNull()))

# COMMAND ----------

#SUBID10022 --> 134184 --> Flu --> S110
#SUBID10049 --> 121783 --> Bladder cancer ---> S107

# COMMAND ----------

sub_df = sub_df.withColumn("Subgrp_id", when((col("Subgrp_id").isNull()) & (col("sub_id") == "SUBID10022"), "S110") \
                                       .when((col("Subgrp_id").isNull()) & (col("sub_id") == "SUBID10049"), "S107") \
                                        .otherwise(col("Subgrp_id")))

# COMMAND ----------

display(sub_df.select("*").filter(col("sub_id") == "SUBID10049"))

# COMMAND ----------

write2silver(sub_df,"Subscriber_S.csv")

# COMMAND ----------

# just adding display function at the end


display(sub_df.limit(10))


