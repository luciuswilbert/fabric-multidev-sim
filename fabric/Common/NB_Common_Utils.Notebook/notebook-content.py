# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   }
# META }

# MARKDOWN ********************

# # NB_Common_Utils
# Shared helpers. Load with `%run NB_Common_Utils`. Changes need the Lead's review (CODEOWNERS).

# CELL ********************

from pyspark.sql import functions as F

def add_audit_columns(df, source):
    """Add the standard Bronze audit columns."""
    return (df
            .withColumn("_src_system", F.lit(source))
            .withColumn("_ingested_at", F.current_timestamp()))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
