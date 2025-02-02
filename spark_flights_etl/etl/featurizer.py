from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession, DataFrame, functions as F


class Featurizer:

    def __init__(self, spark: SparkSession | DatabricksSession, properties: dict):
        self.spark = spark
        self.properties = properties

    def preprocesa(self, df: DataFrame) -> DataFrame:

        concatenado_col = F.concat_ws(" ", "FlightDate", F.lpad(F.col("DepTime"), 4, "0"))
        preprocesado_df = (
            df.fillna(0, subset=["CarrierDelay", "WeatherDelay", "NASDelay", "SecurityDelay", "LateAircraftDelay"])
              .withColumn("Diverted", F.when(F.col("Diverted") == 0.0, False).otherwise(True))
              .withColumn("FlightTs", F.to_timestamp(concatenado_col, format=F.lit("yyyy-MM-dd HHmm")))
        )

        return preprocesado_df
