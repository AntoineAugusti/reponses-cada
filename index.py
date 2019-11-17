import pandas as pd

df = pd.read_csv("cada-2019-11-17.csv")
df = df.loc[df.Type == "Avis"]
df = df.loc[df.Année > 2015]

by_admin = df.Administration.value_counts()
by_admin = by_admin.loc[by_admin > 10]

df = df.loc[df.Avis.fillna("").str.contains("En l'absence de réponse"), :]
no_responses_admin = df.Administration.value_counts()
no_responses_admin = no_responses_admin.loc[by_admin.index]

pct = (no_responses_admin / by_admin).fillna(1).sort_values()

final = pd.concat(
    [pct.round(2).rename("pourcentage_reponse"), by_admin.rename("nb_demandes")],
    axis=1,
    sort=False,
).sort_values(by="nb_demandes", ascending=False)
final.index.name = "administration"
final.to_csv("data.csv")
