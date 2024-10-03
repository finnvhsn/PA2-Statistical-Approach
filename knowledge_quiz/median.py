import numpy as np

# data
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]
infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# Median
median_video = np.median(video_group_scores)
median_infographic = np.median(infographic_group_scores)

print(f"Median der Videos-Gruppe: {median_video}")
print(f"Median der Infografiken-Gruppe: {median_infographic}")

# which group is better
if median_video > median_infographic:
    print("Die Videos-Gruppe hat besser abgeschnitten.")
elif median_video < median_infographic:
    print("Die Infografiken-Gruppe hat besser abgeschnitten.")
else:
    print("Beide Gruppen haben gleich abgeschnitten.")

"""
results: 
Median der Videos-Gruppe: 13.5
Median der Infografiken-Gruppe: 15.0
Die Infografiken-Gruppe hat besser abgeschnitten.
"""