import matplotlib.pyplot as plt
import numpy as np

# mean and standard deviation
mean_videos = 12.71875
std_videos = 2.2946949688357274
mean_infographics = 14.625
std_infographics = 1.161895003862225

# preparing data
categories = ['Video', 'Infografik']
means = [mean_videos, mean_infographics]
stds = [std_videos, std_infographics]

# evaluate bar chart
plt.figure(figsize=(10, 5))
plt.bar(categories, means, yerr=stds, capsize=10, color=['blue', 'green'])

# descriptions
plt.title('Mittelwert der Punkte mit Standardabweichung')
plt.ylabel('Durchschnittliche Punktzahl')
plt.ylim(0, 16) 
plt.show()
