import numpy as np

# data
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]
infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# Median
median_video = np.median(video_group_scores)
median_infographic = np.median(infographic_group_scores)

print(f"median of video group: {median_video}")
print(f"median of infographic group: {median_infographic}")

# which group is better
if median_video > median_infographic:
    print("the video group performed better.")
elif median_video < median_infographic:
    print("the infographic group performed better.")
else:
    print("both groups performed the same.")

"""
results: 
Median of video group: 13.5
Median of infographic group: 15.0
The infographic group performed better
"""