from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession, DataFrame


class Featurizer:

    def __init__(self, spark: SparkSession | DatabricksSession, properties: dict):
        self.spark = spark
        self.properties = properties

    def preprocesa(self, df: DataFrame) -> DataFrame:
        # elimina este error y añade aquí tu código
        raise NotImplementedError
