from etl.featurizer import Featurizer


class FlujoDiario:
    """
    ETL diaria
    """

    def __init__(self, spark, properties: dict):
        self.properties = properties
        self.spark = spark

    def run(self):
        # podríamos recuperar la SparkSession activa desde cualquier DF o bien con SparkSession.builder.getOrCreate()
        # porque se comporta de manera similar a un Singleton (objeto del que solo existe una instancia en nuestro
        # programa), aunque no es exactamente un Singleton ya que en casos particulares, es posible crear varias
        # sesiones al mismo tiempo:
        # https://medium.com/analytics-vidhya/spark-session-and-the-singleton-misconception-1aa0eb06535a

        # storage_account_name = self.properties["STORAGE_ACCOUNT_NAME"]

        # si necesitas leer, lo ideal es usar una
        # propiedad del fichero de configuración, que podemos llamar por ejemplo STORAGE_ACCOUNT_NAME
        flights_df = (self.spark.read
            # Si estás usando Databricks Free Edition, necesitarás indicar la clave de acceso a tu cuenta de almacenamiento
            # de Azure cada vez que quieras leer , ya que Free Edition no permite editar las propiedades
            # del cluster para configurar ahí la clave para todas las lecturas.
            #.option("fs.azure.account.key.tu_storage_account_aquí.dfs.core.windows.net",
            #        "tu_api_key_aquí")
            .option("header", "true")
            .option("inferSchema", "true")
            .csv(self.properties["raw_input_file"])
        )

        featurizer = Featurizer(self.spark, self.properties)
        preprocesado_df = featurizer.preprocesa(flights_df)
        preprocesado_df.show()



