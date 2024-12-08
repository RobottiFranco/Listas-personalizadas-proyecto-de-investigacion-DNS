import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.cm import get_cmap
from Clases.helper.globalVariables import category_code

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


    def guardarGraficoMejorado(self, archivo_salida: str, formato="png") -> None:
        try:
            self.graficarBarrasAnomaliasMejorado() 
            plt.savefig(archivo_salida, format=formato)
            plt.close()
            print(f"Gráfico guardado como {archivo_salida}")
        except Exception as e:
            print(f"Error al guardar el gráfico: {e}")

            
    def graficarBarrasAnomaliasMejorado(self) -> None:
        categorias = [item["category_code"] for item in self.datos if item["category_code"] in category_code]
        anomalies = [item["anomaly_count"] for item in self.datos if item["category_code"] in category_code]

        sorted_data = sorted(zip(categorias, anomalies), key=lambda x: x[1], reverse=True)
        categorias, anomalies = zip(*sorted_data)

        cmap = get_cmap("tab20")  
        colors = [cmap(i) for i in range(len(categorias))]

        plt.figure(figsize=(14, 8))
        bars = plt.bar(categorias, anomalies, color=colors)

        total_anomalies = sum(anomalies)
        for i, value in enumerate(anomalies):
            percentage = f"{(value / total_anomalies) * 100:.1f}%"
            plt.text(i, value + 0.5, f"{value} ({percentage})", ha="center", fontsize=10)

        if self.ooni_run_link_id is None:
            plt.title(f"Conteo de anomalías por categoría para {self.probe_cc} OONI Explorer", fontsize=16)
        else:
            plt.title(f"Conteo de anomalías por categoría para {self.probe_cc} (OONI Link: {self.ooni_run_link_id})", fontsize=16)
        
        plt.xlabel("Categorías", fontsize=14)
        plt.ylabel("Número de anomalías", fontsize=14)
        plt.xticks(rotation=30, ha="right", fontsize=12)
        plt.ylim(0, max(anomalies) + 10)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        legend_handles = [Patch(color=colors[i], label=category_code.get(categorias[i], categorias[i])) for i in range(len(categorias))]
        plt.legend(handles=legend_handles, title="Categorías", bbox_to_anchor=(1.05, 1), loc="upper left")

        plt.tight_layout()
