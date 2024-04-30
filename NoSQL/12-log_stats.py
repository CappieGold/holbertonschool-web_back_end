#!/usr/bin/env python3
"""
    Write a Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient()
db = client.logs
collection = db.nginx

# Nombre total de documents dans la collection
total_logs = collection.count_documents({})

# Nombre de documents avec chaque méthode
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Nombre de documents avec method=GET et path=/status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Affichage des statistiques
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
print(f"{status_check_count} status check")
