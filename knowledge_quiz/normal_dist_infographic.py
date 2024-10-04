import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import gaussian_kde

# Punktwerte für die Infografik-Gruppe
infographic_group_scores = [14, 13, 16, 13.5, 15, 12, 14, 14.5, 15, 15, 14, 16, 15, 16, 15, 16]

data = infographic_group_scores

mean = np.mean(data)
std_dev = np.std(data)

# Erstelle ein Histogramm mit Bin-Größe 0,5, und setze die Bins explizit von 8 bis 16,5
plt.figure(figsize=(10, 5))
count, bins, ignored = plt.hist(data, bins=np.arange(8, 17, 0.5), density=False, alpha=0.6, color='green', edgecolor='black')

# Berechne die Normalverteilungskurve
xmin, xmax = plt.xlim()  # x-Bereich der Grafik ermitteln
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)

# Berechne die tatsächliche Dichteverteilung (KDE - Kernel Density Estimate)
kde = gaussian_kde(data)
kde_values = kde(x)

# Zeichne die Normalverteilungskurve
plt.plot(x, p * max(count), 'k', linewidth=2, label='Normalverteilung')

# Zeichne die tatsächliche Verteilung (KDE)
plt.plot(x, kde_values * max(count), 'r--', linewidth=2, label='Tatsächliche Verteilung')

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Normalverteilung und Punktverteilung (Infografik-Gruppe)')
plt.xlabel('Punkte')
plt.ylabel('Häufigkeit')

# Zeige die Skala auf der x-Achse mit 0,5-Schritten an
plt.xticks(np.arange(8, 16.5, 0.5))

# Legende hinzufügen
plt.legend()

# Zeige die Grafik an
plt.show()
