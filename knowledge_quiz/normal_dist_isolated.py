import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import gaussian_kde

# Mittelwert und Standardabweichung für beide Gruppen
mean_video = 12.71875
std_dev_video = 2.2946949688357274

mean_infographic = 14.625
std_dev_infographic = 1.161895003862225

# Daten für die Video- und Infografik-Gruppen
video_group_scores = [14, 8, 9, 14, 13, 12.5, 14, 8, 13, 15, 14, 13, 13, 15, 14, 14]
infographic_group_scores = [14, 13, 16, 13.5, 15, 12, 14, 14.5, 15, 15, 14, 16, 15, 16, 15, 16]

# Erstelle eine Reihe von X-Werten (z.B. von 8 bis 16) für das Diagramm
x_values = np.linspace(8, 16, 100)

# Berechne die Normalverteilung für beide Gruppen
pdf_video = norm.pdf(x_values, mean_video, std_dev_video)
pdf_infographic = norm.pdf(x_values, mean_infographic, std_dev_infographic)

# Berechne die tatsächliche Verteilung (KDE) für beide Gruppen
kde_video = gaussian_kde(video_group_scores)
kde_values_video = kde_video(x_values)

kde_infographic = gaussian_kde(infographic_group_scores)
kde_values_infographic = kde_infographic(x_values)

# Erstelle das Diagramm
plt.figure(figsize=(10, 6))

# Normalverteilung der Video-Gruppe
plt.plot(x_values, pdf_video, label='Normalverteilung (Video-Gruppe)', color='blue')

# Tatsächliche Verteilung der Video-Gruppe
plt.plot(x_values, kde_values_video, 'b--', label='Tatsächliche Verteilung (Video-Gruppe)', linewidth=2)

# Normalverteilung der Infografik-Gruppe
plt.plot(x_values, pdf_infographic, label='Normalverteilung (Infografik-Gruppe)', color='green')

# Tatsächliche Verteilung der Infografik-Gruppe
plt.plot(x_values, kde_values_infographic, 'g--', label='Tatsächliche Verteilung (Infografik-Gruppe)', linewidth=2)

# Titel und Achsenbeschriftungen hinzufügen
plt.title('Normalverteilungen und Tatsächliche Verteilungen der Gruppen')
plt.xlabel('Punkte')
plt.ylabel('Wahrscheinlichkeitsdichte')

# Legende hinzufügen
plt.legend()

# Zeige die Grafik an
plt.show()
