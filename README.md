# Annalyse de l'irradiation solaire en France par commune

## Description et Portée

Ce projet vise à fournir des données d'irradiation solaire pour les communes françaises, ainsi que des outils pour l'analyse et la génération de classements. Les données sont mises à jour régulièrement et sont destinées à être utilisées pour des études énergétiques, des projets de développement durable et des analyses géospatiales. La portée de ce projet inclut la collecte, le traitement et la mise à disposition de données d'irradiation, ainsi que le développement de scripts et de notebooks pour faciliter leur exploitation.



## Comment citer

Si vous utilisez ces données ou outils dans vos travaux, veuillez les citer comme suit :

### APA

SolaireSimple (2025). *Données d'irradiation solaire et outils d'analyse*. [https://solairesimple.fr/datasets].

### BibTeX

```bibtex
@misc{arbo2025,
  author = {{SolaireSimple}},
  title = {{Données d'irradiation solaire et outils d'analyse}},
  year = {2025},
  url = {[https://solairesimple.fr/datasets]}
}
```



## Exemple d'usage (Python snippet)

Voici un exemple simple d'utilisation des données d'irradiation avec Python :

```python
import pandas as pd

# Charger les données
data_path = 'data/irradiation_communes_2025_07.csv'
df = pd.read_csv(data_path)

# Afficher les premières lignes
print(df.head())

# Exemple de calcul : irradiation moyenne
# mean_irradiation = df['Irradiation annuelle (kWh/m²)'].mean()
# print(f"Irradiation annuelle moyenne : {mean_irradiation:.2f} kWh/m²")
```

## Données

Retrouvez ce jeu de données et d'autres ressources sur notre portail :

[Données d'irradiation solaire par commune](https://solairesimple.fr/datasets)

## 🎁 Widget irradiation solaire (iframe)

Ajoutez en 30 secondes un encart “irradiation & ROI” à n’importe quel blog WordPress, page Notion ou site HTML :  

```html
<iframe
  src="https://solairesimple.fr/widget/irradiation?insee=75001"
  width="300"
  height="420"
  style="border:0;border-radius:12px;max-width:100%;"
  loading="lazy"
></iframe>
```

Fonctionnalités:

- Irradiation annuelle, ROI, économies, CO₂ évité
- Responsive : ≤ 20 kB, aucun cookie, HTTPS only
- Licence CC-BY 4.0 : attribution “Propulsé par SolaireSimple” déjà incluse
- Paramètres : insee (préféré) ou code postal, option ref= pour suivre vos intégrations

👉 Documentation complète : https://solairesimple.fr/widget/

## Release tag v2025.07 + changelog

Cette version correspond à la release `v2025.07`.

Pour consulter l'historique des modifications, veuillez vous référer au fichier [CHANGELOG.md](https://github.com/open-solar-france/open-solar-france/blob/main/Changelog.md).

