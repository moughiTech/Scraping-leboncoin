# Scraping-leboncoin (The readme file is written in both french and english)

_English description

Scrapy is used to extract real estate offers in the city of Massy in france and uses MongoDB for the storage of this data.
The scraping has been made with regards to the website's ROBOT.txt' policies. 

The extraction of the web content made use of a pipeline of two modules (spiders):
- urlExtractor: for the extraction of urls that contain the data
- contentScrapper: to extract the data (Name of the offer, Description, surface, price, etc...)

_French description

Ce projet utilise Scrapy pour extraire les annonces de l'immobilier dans la ville Massy en france et utilise MongoDb pour les stocker. 
Le scraping se fait avec respect des directives figurant dans le fichier ROBOT.txt

L'extraction des données passe par deux spider en cascade: 
- urlExtractor: pour extraire les urls des pages contenant les données
- contentScrapper: pour extraire les données (Nom de l'annonce, Description, prix, etc...)
