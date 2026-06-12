# Databricks notebook source
claims_df = claims_df.replace("NaN",None)
claims_df = claims_df.fillna({"Claim_Or_Rejected":"N"})
claims_df = claims_df.withColumn("claim_amount", claims_df['claim_amount'].cast("integer"))
claims_df = claims_df.withColumn("claim_date", claims_df['claim_date'].cast("date"))