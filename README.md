# Visualisation de population

---

## Prérequis

- **Python** 3.8 ou supérieur.
- **pip** (outil de gestion des packages Python).

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

### 5. Téléchargement des Bases de Données dans le répertoire data

#### 1. Population en 2021 (Données Carroyées - IRIS)

- **Source :** [Données carroyées - Recensement 2021 (INSEE)](https://www.insee.fr/fr/statistiques/8272002)  
- **Fichier :** `rp2021_carreaux_1km_gpkg.zip`  
- **Description :**  
  Données carroyées de population en 2021. Chaque carreau représente une unité spatiale d'1 km².

---

#### 2. Contours des IRIS (Base Infracommunale - IRIS)

- **Source :** [Contours des IRIS - GeoPF](https://data.geopf.fr/telechargement/download/CONTOURS-IRIS/CONTOURS-IRIS_3-0__GPKG_LAMB93_FXX_2024-01-01/CONTOURS-IRIS_3-0__GPKG_LAMB93_FXX_2024-01-01.7z)  
- **Fichier :** `CONTOURS-IRIS_3-0__GPKG_LAMB93_FXX_2024-01-01.7z`  
- **Description :**  
  Ce produit permet de faire le lien entre les données cartographiques et les données statistiques de l’INSEE. Chaque IRIS est une entité géographique infracommunale.

---

#### 3. Population en 2021 (Base Infracommunale - IRIS)

- **Source :** [Recensement de la Population 2021 - INSEE](https://www.insee.fr/fr/statistiques/8268806)  
- **Fichier :** `base-ic-evol-struct-pop-2021_csv.zip`  
- **Description :**  
  Base de données contenant des informations détaillées sur la population à l'échelle infracommunale (IRIS) pour l'année 2021.

---

#### 4. Logement en 2021 (Base Infracommunale - IRIS)

- **Source :** [Recensement des Logements 2021 - INSEE](https://www.insee.fr/fr/statistiques/8268838)  
- **Fichier :** `base-ic-logement-2021_csv.zip`  
- **Description :**  
  Informations sur les logements à l'échelle infracommunale pour l'année 2021.

---

#### 5. Revenus, Pauvreté et Niveau de Vie en 2019 (Filosofi - Données Carroyées)

- **Source :** [Dispositif Fichier Localisé Social et Fiscal (Filosofi)](https://www.insee.fr/fr/statistiques/7655475?sommaire=7655515)  
- **Fichiers :** `Filosofi2019_carreaux_200m_gpkg.zip`
- **Description :**  
  Ce fichier contient des données détaillées sur les revenus, la pauvreté et le niveau de vie pour l'année 2019 :

#### 6. DPE (avant juillet 2021) pour le département 33 (Gironde)

- **Source :** [data.ademe.fr](https://data.ademe.fr/datasets/dpe-33)
- **Fichier :** `dpe-33.csv`
- **Description :**
  Le DPE décrit le bâtiment ou le logement (surface, orientation, murs, fenêtres, matériaux, etc)

### 6. Décompresser les basses de données dans le répertoire data à l'aide d'un gestionnaire de fichier

### 7. Lancer Jupyter Notebook

```bash
jupyter notebook coord_to_addr.ipynb
```
