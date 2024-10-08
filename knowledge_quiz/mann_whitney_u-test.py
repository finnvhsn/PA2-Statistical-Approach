import scipy.stats as stats

# data
video_group_scores = [14,8,9,14,13,12.5,14,8,13,15,14,13,13,15,14,14]
infographic_group_scores = [14,13,16,13.5,15,12,14,14.5,15,15,14,16,15,16,15,16]

# Mann-Whitney-U-Test
mannwhitney_stat, mannwhitney_p = stats.mannwhitneyu(video_group_scores, infographic_group_scores)

# results
print(f"Mann-Whitney-u-test: teststatistic = {mannwhitney_stat}, p-value = {mannwhitney_p}")

"""
results:    Mann-Whitney-u-test: teststatistic = 53.0, p-value = 0.004201092389217708
"""