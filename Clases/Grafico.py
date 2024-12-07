import matplotlib.pyplot as plt

class Grafico:
    def __init__(self, datos, probe_cc: str, ooni_run_link_id: int = None):
        self.datos = datos.get("result", [])
        self.probe_cc = probe_cc
        self.ooni_run_link_id = ooni_run_link_id
            
    def graficarBarrasAnomalias(self) -> None:
        categorias = [item["category_code"] for item in self.datos]
        anomalies = [item["anomaly_count"] for item in self.datos]

        plt.figure(figsize=(12, 6))
        plt.bar(categorias, anomalies, color='yellow')

        if self.ooni_run_link_id is None:
            plt.title(f"Conteo de anomalías por categoría para {self.probe_cc} OONI explorer", fontsize=16)
        else:
            plt.title(f"Conteo de anomalías por categoría para {self.probe_cc} OONI link: {self.ooni_run_link_id}", fontsize=16)

        plt.xlabel("Categorías", fontsize=14)
        plt.ylabel("Número de anomalías", fontsize=14)

        plt.xticks(rotation=45, ha="right", fontsize=10)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        plt.tight_layout()

    def guardarGrafico(self, archivo_salida: str, formato="png") -> None:
        try:
            self.graficarBarrasAnomalias() 
            plt.savefig(archivo_salida, format=formato)
            plt.close()
            print(f"Gráfico guardado como {archivo_salida}")
        except Exception as e:
            print(f"Error al guardar el gráfico: {e}")