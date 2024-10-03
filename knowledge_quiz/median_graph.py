import numpy as np
import matplotlib.pyplot as plt

# data
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]
infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# Medianwerte
median_video = np.median(video_group_scores)
median_infographic = np.median(infographic_group_scores)

# Balkendiagramm erstellen
plt.figure(figsize=(10, 5))
plt.bar(['Video', 'Infografik'], [median_video, median_infographic], color=['blue', 'green'])
plt.title('Medianvergleich der Punktverteilung')
plt.ylabel('Median der Punkte')
plt.ylim(0, 16)  # Maximale Punktzahl einstellen
plt.show()
