"""
Classe: PR-216	/   Année: 2021-2022   /    Professeur: M.Bah

Membres du Groupe: Mehdi Tage Eddine - Mouhamadou Lamine Diagne

Projet Python: Système de gestion d'un compte bancaire

"""

"""
		Système de gestion d'un compte bancaire

Création d'une classe client

Name = nom
AccountID = Adresse (ID) du compte
Address = Adresse
Phone = Téléphone
Profession = Profession
balance = Etat actuel du Compte = 0 (initiale)
"""
class Client:

	def __init__(self, Name="", AccountID=0, Address="", Phone="", Profession="", balance = 0.0):
		self.Name = Name
		self.AccountID = AccountID
		self.Address = Address
		self.Phone = Phone
		self.Profession = Profession
		self.balance = balance

# Création d'une fonction withdraw -> (retrait) avec paramètre amount -> (montant)
	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeError('Montant supérieur au Solde actuel.')
		self.balance -= amount

# Création d'une fonction deposit -> (dépôt) avec paramètre amount -> (montant)
	def deposit(self, amount):
		self.balance += amount

# Création d'une fonction getbalance -> (info état du compte (solde))
	def getbalance(self):
		return self.balance

# Création d'une fonction getInfo -> (info état global du compte )
	def getInfo(self):
		print("ID:", self.AccountID, \
			  "\t--  Nom_du_Client:", self.Name, \
			  "\t--  Adresse:", self.Address, \
			  "\t--  Tel:", self.Phone, \
			  "\t--  Profession:", self.Profession, \
			  "\t--  Balance:",self.balance)


if __name__ == "__main__":
# Point d'entré du programme

	AccountID = 0
# Création d'un dictionnaire vide -> Account pour stocker de nouveaux comptes créés
	Account = dict()

	while True:
		print("\n **************** Bienvenue chez Virtual Bank ****************\n")

	# option peut recevoir comme valeur une lettre miniscule ou majuscule
		option = input("\t\t\t\t\t\t    MENU \
						\n\t\t\t\t\t\t    ---- \
						\n\t\t\t\t\tC --> Créer un compte \
						\n\t\t\t\t\tD --> Dépot \
						\n\t\t\t\t\tR --> Retrait \
						\n\t\t\t\t\tS --> Solde Bancaire \
						\n\t\t\t\t\tV --> Voir Compte \
						\n\t\t\t\t\tQ --> Quitter  \
						\n\t\t\t-----------------------------------\
						\n\t\t\t\t\tFaites votre choix : ")
		print("\n*******************************  *******************************")

		if( option  == "C" or option == "c"):

			Name = input("Entrer votre nom : ")
			Address = input("Entrer votre Adresse : ")
			Phone = input("Entrer votre Numéro de téléphone : ")
			Profession = input("Entrer votre Profession : ")

			client = Client(Name, AccountID, Address, Phone, Profession)
		# Une mise à jour des comptes des clients avec leurs ID (dans l'ordre croissant) par la fonction update
			Account.update({AccountID : client})
			print("\n*************************************")
			print("\t  Compte Créé avec succès !");
			print("*************************************")

			print("\nID :", AccountID, \
				  "\nNom_du_client :", Name, \
				  "\nAdresse :", Address, \
				  "\nTéléphone :", Phone, \
				  "\nProfession :", Profession)

			AccountID += 1

		elif(option == "R" or option == "r"):

			temp_AccountID = int(input("Entrez votre ID : "))
			withDrawAmount = float(input("Entrez le montant à retirer : "))
	# avec (try) : si la condition posée n'est pas vérifiée, (except) est exécuté
			try:
				client = Account[temp_AccountID]
				client.withdraw(withDrawAmount)
				print("\n*********************************")
				print("\t\tRetrait effectué avec succès !")
				print("*************************************")

				print("\nVous avez effectué un retrait de : ", withDrawAmount)
				print("\nVotre nouveau solde est de : ", client.getbalance())
			except:
				print("Error: Montant supérieur au Solde actuel.")

		elif(option == "D" or option == "d"):
			temp_AccountID = int(input("Entrez votre ID : "))
			depositAmount = float(input("Entrez le montant a déposer : "))
			try:
				client = Account[temp_AccountID]
				client.deposit(depositAmount)
				print("\n************************************")
				print("\tDépot effectué avec succès !")
				print("*************************************")

				print("\nVous avez effectué un dépot de : ", depositAmount)
				print("\nVotre nouveau solde est de : ", client.getbalance());
			except:
				print("Error:");

		elif(option == "S" or option == "s"):
			temp_AccountID = int(input("Entrez votre ID : "))
			try:
				client = Account[temp_AccountID]
				print("\n*********************************");
				print("\nVotre solde est de : ", client.getbalance());
			except:
				print("Error:")

		elif(option == "V" or option == "v"):
			for x in range(len(Account)) :
				client = Account[x]
				client.getInfo()

		elif(option == "Q" or option == "q"):
	# (break) -> fin du programme
			break;
