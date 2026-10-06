import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("SalesPredict AI — Projet prêt !")

# Générateur aléatoire reproductible
rng = np.random.default_rng(42)

# Historique de 730 jours
nombre_jours = 730
dates = pd.date_range(start="2024-01-01", periods=nombre_jours, freq="D")
jours = np.arange(nombre_jours)

# Trois éléments influencent nos ventes fictives
tendance = 0.05 * jours
cycle_semaine = 20 * np.sin(2 * np.pi * jours / 7)
bruit = rng.normal(loc=0, scale=8, size=nombre_jours)

# Base de 100 articles par jour, avec les variations ci-dessus
ventes = 100 + tendance + cycle_semaine + bruit
ventes = np.maximum(0, np.round(ventes)).astype(int)

# Tableau contenant notre historique
df = pd.DataFrame({
    "date": dates,
    "ventes": ventes
})

print(df.head(10))
print("Nombre de lignes :", len(df))

# Moyenne des ventes sur les 7 derniers jours
moyenne_mobile = df["ventes"].rolling(window=7).mean()

# Création du graphique
plt.figure(figsize=(12, 5))

plt.plot(
    df["date"], df["ventes"],
    label="Ventes quotidiennes", color="royalblue", alpha=0.4
)

plt.plot(
    df["date"], moyenne_mobile,
    label="Moyenne sur 7 jours", color="darkorange", linewidth=2
)

plt.title("Historique des ventes — Données fictives")
plt.xlabel("Date")
plt.ylabel("Nombre d’articles vendus")
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()