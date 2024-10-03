import seaborn as sns
import matplotlib.pyplot as plt

video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]
infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# Daten vorbereiten
data = video_group_scores + infographic_group_scores
groups = ['Video'] * len(video_group_scores) + ['Infografik'] * len(infographic_group_scores)

# Violinplot erstellen
plt.figure(figsize=(10, 5))
sns.violinplot(x=groups, y=data)
plt.title('Violinplot der Punktverteilung für Video und Infografik')
plt.ylabel('Punkte')
plt.ylim(0, 16)  # Maximale Punktzahl einstellen
plt.show()
