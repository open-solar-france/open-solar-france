#!/usr/bin/env python3
"""
Script pour générer des classements basés sur les données d'irradiation solaire.

Ce script lit les données d'irradiation des communes françaises et génère
différents types de classements pour faciliter l'analyse.

Auteur: SolaireSimple
Version: v2025.01
"""

import pandas as pd
import numpy as np
import argparse
import sys
from pathlib import Path


def load_irradiation_data(file_path):
    """
    Charge les données d'irradiation depuis un fichier CSV.
    
    Args:
        file_path (str): Chemin vers le fichier CSV
        
    Returns:
        pd.DataFrame: DataFrame contenant les données d'irradiation
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Données chargées avec succès : {len(df)} communes")
        return df
    except FileNotFoundError:
        print(f"Erreur : Fichier {file_path} non trouvé")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors du chargement des données : {e}")
        sys.exit(1)


def generate_top_ranking(df, column_name, top_n=50):
    """
    Génère un classement des communes avec la plus forte irradiation.
    
    Args:
        df (pd.DataFrame): DataFrame des données
        column_name (str): Nom de la colonne d'irradiation
        top_n (int): Nombre de communes à inclure dans le classement
        
    Returns:
        pd.DataFrame: DataFrame du classement
    """
    if column_name not in df.columns:
        print(f"Erreur : Colonne '{column_name}' non trouvée dans les données")
        return None
    
    ranking = df.nlargest(top_n, column_name).reset_index(drop=True)
    ranking.index += 1  # Commencer le classement à 1
    return ranking


def generate_regional_ranking(df, region_column, irradiation_column):
    """
    Génère un classement par région.
    
    Args:
        df (pd.DataFrame): DataFrame des données
        region_column (str): Nom de la colonne région
        irradiation_column (str): Nom de la colonne d'irradiation
        
    Returns:
        pd.DataFrame: DataFrame du classement régional
    """
    if region_column not in df.columns or irradiation_column not in df.columns:
        print(f"Erreur : Colonnes manquantes pour le classement régional")
        return None
    
    regional_stats = df.groupby(region_column)[irradiation_column].agg([
        'mean', 'median', 'std', 'count'
    ]).round(2)
    
    regional_stats.columns = ['Moyenne', 'Médiane', 'Écart-type', 'Nb_communes']
    regional_stats = regional_stats.sort_values('Moyenne', ascending=False)
    
    return regional_stats


def save_ranking(ranking, output_path, title):
    """
    Sauvegarde un classement dans un fichier CSV.
    
    Args:
        ranking (pd.DataFrame): DataFrame du classement
        output_path (str): Chemin de sortie
        title (str): Titre du classement
    """
    try:
        ranking.to_csv(output_path, index=True)
        print(f"{title} sauvegardé dans : {output_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")


def main():
    """Fonction principale du script."""
    parser = argparse.ArgumentParser(
        description="Génère des classements basés sur les données d'irradiation"
    )
    parser.add_argument(
        "--input", 
        default="data/irradiation_communes_2025_07.csv",
        help="Chemin vers le fichier de données d'entrée"
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Répertoire de sortie pour les classements"
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=50,
        help="Nombre de communes dans le classement principal"
    )
    
    args = parser.parse_args()
    
    # Créer le répertoire de sortie
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Charger les données
    df = load_irradiation_data(args.input)

    irradiation_col = "Irradiation annuelle (kWh/m²)"
    region_col = "Region"
    commune_col = "Commune"
    
    # Vérifier que les colonnes existent (exemple)
    print("Colonnes disponibles dans le fichier :")
    print(df.columns.tolist())
    
    # Générer le classement principal
    if irradiation_col in df.columns:
        top_ranking = generate_top_ranking(df, irradiation_col, args.top_n)
        if top_ranking is not None:
            save_ranking(
                top_ranking,
                output_dir / f"top_{args.top_n}_communes_irradiation.csv",
                f"Top {args.top_n} des communes"
            )
    
    if region_col in df.columns and irradiation_col in df.columns:
        regional_ranking = generate_regional_ranking(df, region_col, irradiation_col)
        if regional_ranking is not None:
            save_ranking(
                regional_ranking,
                output_dir / "classement_regional_irradiation.csv",
                "Classement régional"
            )
    
    print("Génération des classements terminée !")


if __name__ == "__main__":
    main()

