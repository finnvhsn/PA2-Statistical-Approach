import scipy.stats as stats

"Testing the normal distribution in order to decide weather the t-test or the u-test is to be applied."

# Deine Punktdaten für die beiden Gruppen
video_group_scores = [14, 8, 9, 14, 13, 12.5, 14, 8, 13, 15, 14, 13, 13, 15, 14, 14]
infographic_group_scores = [14, 13, 16, 13.5, 15, 12, 14, 14.5, 15, 15, 14, 16, 15, 16, 15, 16]

# Shapiro-Wilk-Test für Normalverteilung
shapiro_video = stats.shapiro(video_group_scores)
shapiro_infographic = stats.shapiro(infographic_group_scores)

# Ergebnisse anzeigen
print(f"Shapiro-Wilk-Test für Video-Gruppe: Teststatistik = {shapiro_video[0]}, p-Wert = {shapiro_video[1]}")
print(f"Shapiro-Wilk-Test für Infografik-Gruppe: Teststatistik = {shapiro_infographic[0]}, p-Wert = {shapiro_infographic[1]}")

p_value_video = shapiro_video[1]
p_value_infographic = shapiro_infographic[1]


if p_value_video < 0.05:
    print("the results from the video group are not normally distributed.")
else:
    print("the results from the video group are normally distributed.")
    
if p_value_infographic < 0.05:
    print("the results from the infographic group are not normally distributed.")
else:
    print("the results from the infographic group are normally distributed.")


"""
results: 
Shapiro-Wilk-Test for video-group: teststatistic = 0.7541551392370752, p-value = 0.0007131874146155824
Shapiro-Wilk-Test for infographic-group: teststatistic = 0.9140617609587363, p-value = 0.13531743697865667
the results from the video group are not normally distributed.
the results from the infographic group are normally distributed.
"""