import numpy as np

# Data of groups
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]

infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# calculation of mean scores
mean_video_group = np.mean(video_group_scores)
mean_infographic_group = np.mean(infographic_group_scores)

print(mean_video_group)
print(mean_infographic_group)

