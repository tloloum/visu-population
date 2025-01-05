# Visualisation de population

---

## Prérequis

- **Python** 3.8 ou supérieur.
- **pip** (outil de gestion des packages Python).
- **Jupyter Notebook** ou **JupyterLab**.

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/tloloum/visu-population.git
cd visu-population
```

### 2. Créer un environnement virtuel

Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet.

```bash
python -m venv env # avec "env" le chemin du dossier de l'environnement virtuel
source env/bin/activate # linux/macOS
env\Scripts\activate # windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer Jupyter Notebook

```bash
jupyter notebook coord_to_addr.ipynb
```

## Data

### 1. Population en 2021 (Base infracommunale - IRIS)

- **Source :** [Recensement de la population 2021 - INSEE](https://www.insee.fr/fr/statistiques/8268806)
- **Fichier :** `base-ic-evol-struct-pop-2021_csv.zip`
- **Description :**  
  Base de données contenant des informations détaillées sur la population à l'échelle infracommunale
  (IRIS) pour l'année 2021.

---

### 2. Population en 2021 (Données Carroyées)

- **Source :** [Données carroyées - Recensement 2021](https://www.insee.fr/fr/statistiques/8272002)
- **Fichier :** `rp2021_carreaux_1km_gpkg.zip`
- **Description :**  
  Données carroyées de population en 2021. Chaque carreau représente une unité spatiale d'1 km².

---

### 3. Logement en 2021 (Base infracommunale - IRIS)

- **Source :** [Recensement des logements 2021 - INSEE](https://www.insee.fr/fr/statistiques/8268838)
- **Fichier :** `base-ic-logement-2021_csv.zip`
- **Description :**  
  Informations sur les logements à l'échelle infracommunale pour l'année 2021.

---

### 4. Revenus et Niveau de Vie en 2019 (Données Carroyées)

- **Source :** [Filosofi - INSEE (2019)](https://www.insee.fr/fr/statistiques/7655475?sommaire=7655515)
- **Fichiers :**
  - `Filosofi2019_carreaux_200m_gpkg.zip`
  - `Filosofi2019_carreaux_nivNaturel_gpkg.zip`
- **Description :**  
  Données carroyées (200m² et niveau naturel) sur les revenus, la pauvreté et le niveau de vie en 2019.
  Ces données sont issues du dispositif Filosofi.

### Documentation

- Les variables de chaque jeu de données sont accessibles depuis les liens INSEE ci-dessus.
- Les méthodes de calcul et les définitions des indicateurs sont également disponibles sur le site de l'INSEE.

## Remarques

- Les fichiers volumineux (supérieurs à 50 Mo) sont suivis via **Git LFS**.
- En cas de besoin, ces fichiers peuvent être téléchargés directement depuis les liens INSEE ci-dessus.
- Les données carroyées permettent des analyses spatiales à différentes échelles (1 km², 200 m²).
