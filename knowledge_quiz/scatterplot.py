import matplotlib.pyplot as plt

# Data of groups
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]

infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# creation of scatterplot
plt.figure(figsize=(10, 5))

# scatterplot for video group
plt.scatter([1] * len(video_group_scores), video_group_scores, color='blue', label='Video Gruppe', alpha=0.7, marker='x') #alpha 0.7 for transparency of points


# scatterplot for infographic group
plt.scatter([2] * len(infographic_group_scores), infographic_group_scores, color='green', label='Infografik Gruppe', alpha=0.7, marker='x')

# axis and descriptions 
plt.xticks([1, 2], ['Video', 'Infografik'])
plt.title('Streudiagramm der Punktzahlen für beide Gruppen')
plt.ylabel('Punktzahl')
plt.ylim(0, 18)

# legend
plt.legend()

# show diagram
plt.show()

