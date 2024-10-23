import os

class FileManager:
    def __init__(self, file_path):
        """
        Initialise le gestionnaire de fichiers avec le chemin du fichier.
        
        :param file_path: Chemin du fichier texte à gérer.
        """
        self.file_path = file_path

    def read_file(self):
        
        if not os.path.exists(self.file_path):
            print(f"Le fichier '{self.file_path}' n'existe pas.")
            return
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("Contenu du fichier :")
        print(content)

    def write_to_file(self, data):
        """
        Écrit des données dans le fichier texte.

        :param data: Chaîne de caractères à écrire dans le fichier.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Les données ont été écrites avec succès dans le fichier '{self.file_path}'.")

    def count_lines(self):
        """
        Retourne le nombre de lignes dans le fichier texte.

        :return: Nombre de lignes dans le fichier, ou None si le fichier n'existe pas.
        """
        if not os.path.exists(self.file_path):
            print(f"Le fichier '{self.file_path}' n'existe pas.")
            return None
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        num_lines = len(lines)
        print(f"Le fichier '{self.file_path}' contient {num_lines} ligne(s).")
        return num_lines

    def search_keyword(self, keyword):
        """
        Recherche un mot-clé dans le fichier et affiche les lignes correspondantes.

        :param keyword: Mot-clé à rechercher dans le fichier.
        :return: Liste des lignes contenant le mot-clé.
        """
        if not os.path.exists(self.file_path):
            print(f"Le fichier '{self.file_path}' n'existe pas.")
            return None
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        matching_lines = [line.strip() for line in lines if keyword in line]
        
        if matching_lines:
            print(f"Lignes contenant le mot-clé '{keyword}' :")
            for line in matching_lines:
                print(line)
        else:
            print(f"Aucune ligne ne contient le mot-clé '{keyword}'.")
        
        return matching_lines

# Exemple d'utilisation de la classe FileManager
if __name__ == "__main__":
    chemin_fichier = 'mon_fichier.txt'
    
    # Création d'un objet FileManager
    gestionnaire = FileManager(chemin_fichier)
    
    # Écriture dans le fichier
    gestionnaire.write_to_file("Python est un langage puissant.\nIl est utilisé dans divers domaines.\nPython est également facile à apprendre.")
    
    # Lecture du fichier
    gestionnaire.read_file()
    
    # Compter les lignes dans le fichier
    gestionnaire.count_lines()
    

    # Recherche d'un mot-clé dans le fichier
    gestionnaire.search_keyword("Python")
log_file = 'log.txt'

# Création d'un objet FileManager pour le fichier log.txt
gestionnaire = FileManager(log_file)

# 1. Lire le contenu du fichier log.txt
gestionnaire.read_file()

# 2. Ajouter une nouvelle ligne dans le fichier log
nouvelle_ligne = "INFO: Nouvelle entrée de log ajoutée à " + __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
gestionnaire.write_to_file(nouvelle_ligne)

# 3. Rechercher et afficher toutes les lignes contenant "ERROR"
gestionnaire.search_keyword("ERROR")

# 4. Rechercher et afficher toutes les lignes contenant "INFO"
gestionnaire.search_keyword("INFO")

