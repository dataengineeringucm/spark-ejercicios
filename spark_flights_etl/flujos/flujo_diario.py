from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession

from etl.featurizer import Featurizer


class FlujoDiario:
    """
    ETL diaria
    """

    def __init__(self, spark: SparkSession | DatabricksSession, properties: dict):
        self.properties = properties
        self.spark = spark

    def run(self):
        # podríamos recuperar la SparkSession activa desde cualquier DF o bien con SparkSession.builder.getOrCreate()
        # porque se comporta de manera similar a un Singleton (objeto del que solo existe una instancia en nuestro
        # programa), aunque no es exactamente un Singleton ya que en casos particulares, es posible crear varias
        # sesiones al mismo tiempo:
        # https://medium.com/analytics-vidhya/spark-session-and-the-singleton-misconception-1aa0eb06535a

        flights_df = self.spark.read\
            .option("header", "true")\
            .option("inferSchema", "true")\
            .csv(self.properties["raw_input_file"])

        featurizer = Featurizer(self.spark, self.properties)
        preprocesado_df = featurizer.preprocesa(flights_df)
        preprocesado_df.show()
