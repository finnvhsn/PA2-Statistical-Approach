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


"results: the video group has no normal distribution and the infographic group has. In that case, the u-test is more applicable than the t-test."
