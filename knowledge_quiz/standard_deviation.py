import numpy as np

# Data of groups
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]

infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# Calculation of standard deviation
std_video_group = np.std(video_group_scores, ddof=1)

std_infographic_group = np.std(infographic_group_scores, ddof=1)

print("Video standard deviation =", std_video_group)
print("Infographic standard deviation =", std_infographic_group)


"""
results:
Video standard deviation = 2.2946949688357274
Infographic standard deviation = 1.161895003862225
"""