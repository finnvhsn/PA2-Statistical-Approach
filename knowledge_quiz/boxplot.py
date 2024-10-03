import matplotlib.pyplot as plt

# Data of groups
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]

infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]


# Boxplot erstellen
plt.figure(figsize=(10, 5))
plt.boxplot([video_group_scores, infographic_group_scores], labels=['Video', 'Infografik'])
plt.title('Boxplot der Punktverteilung für beide Gruppen')
plt.ylabel('Punktzahl')
plt.ylim(0, 16)  
plt.show()
