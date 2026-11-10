# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   }
# META }

# MARKDOWN ********************

# # NB_Bronze_Files
# Loads the landing CSVs for this source into `LH_Bronze` (schema from `VL_Files`).
# No IDs in code: everything comes from `VL_Common` and `VL_Files`.

# CELL ********************

%run NB_Common_Utils

# CELL ********************

common = notebookutils.variableLibrary.getLibrary("VL_Common")
src    = notebookutils.variableLibrary.getLibrary("VL_Files")

base = f"abfss://{common.data_workspace_id}@onelake.dfs.fabric.microsoft.com/{common.bronze_lakehouse_id}"

for table in src.tables.split(","):
    df = (spark.read.option("header", True).option("inferSchema", True)
          .csv(f"{base}/Files/landing/{src.source_schema}/{table}.csv"))
    df = add_audit_columns(df, src.source_schema)
    (df.write.mode(src.load_mode).option("overwriteSchema", "true").format("delta")
       .save(f"{base}/Tables/{src.source_schema}/{table}"))
    print(f"{src.source_schema}.{table}: {df.count()} rows")
