# Analyse des Ventes FY 2020-2021  
**Optimisation des Stocks & Amélioration de la Rétention Client**

## Description du Projet

Projet d’analyse des ventes en ligne sur les exercices 2020 et 2021 dans le but d’optimiser la gestion des stocks et d’améliorer la rétention client.  
L’analyse suit la méthodologie **CRISP-DM** et se matérialise dans un **dashboard Power BI interactif** avec des mesures DAX.

## Résultats Clés (extrait du dashboard)

| Métrique                              | Valeur observée              | Commentaire principal                                      |
|---------------------------------------|------------------------------|------------------------------------------------------------|
| Nombre de clients uniques             | **~64 255**                  | Base clients significative                                 |
| Quantité maximale commandée (1 ligne) | **501**                      | Pic exceptionnel (probable commande B2B ou promo massive)  |
| Quantité minimale                     | **1**                        | Comportement standard                                      |
| Revenu total période                  | **~498 M$**                  | (≈248 M$ Femmes + 249 M$ Hommes)                           |
| Répartition Hommes / Femmes           | **50,08% F – 49,92% M**      | Quasi-parité très équilibrée                               |
| Meilleure région                      | **South**                    | Nettement devant Midwest, West, Northeast                  |
| Catégorie la plus performante         | **Mobiles & Accessories**    | Très loin devant les autres catégories                     |
| Taux de remise moyen le plus élevé    | Entertainment / Superstore / Appliances | Jusqu’à ~150–170% (vérifier cohérence des données) |
| Tranche d’âge la plus contributive    | **30–39 ans**                | Suivie de 60–69, 40–49, 50–59…                             |
| Évolution AOV                         | 2020 : ~2 307 $ → 2021 : ~2 561 $ | +11 % environ (amélioration panier moyen)          |

## Objectifs du Projet (réalisés)


1. Identification des **Top produits / catégories** pour prioriser stocks & promotions  
   → **Mobiles & Accessories** domine très largement le CA

2. Segmentation client (**RFM en cours / à finaliser**)  
   → Premiers axes d’analyse : âge, genre, région, statut BI (Gross / Net / Valid)

## Modélisation des Données

Après la phase de nettoyage et de préparation, les données ont été restructurées , optimisé pour Power BI et les performances DAX.

### Tables principales du modèle

| Table               | Description principale                                      | 
|-------------------  |-------------------------------------------------------------|
| **Dim_Customers**   |  Référentiel clients (un enregistrement par cust_id)        |
| **Dim_Products**    |  Référentiel produits et catégories                         |




## KPIs Calculés (mesures DAX principales)

```dax
Total Revenue = 
SUMX(
    Sales,
    Sales[qty_ordered] * Sales[price]
)

AOV = 
DIVIDE(
    [Total Revenue],
    DISTINCTCOUNT(Sales[order_id]),
    0
)



Avg Discount Rate % = 
AVERAGE(Sales[discount_percent])

Avg Discount Rate (pondéré) = 
DIVIDE(
    SUM(Sales[discount_amount]),
    [Total Revenue],
    0
)
