
# Commandes
help:
	@echo "Commandes disponibles:"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "Utilisez 'make <commande>' avec une des commandes ci-dessus."
.PHONY: help


start: ## Démarrage de l'application
	@echo "Démarrage de l'application..."
	@. .venv/bin/activate && python3.13 -m bloc64
.PHONY: start


install: ## Installation des dépendances
	@if [ -d ".venv" ]; then \
		echo "Suppression de l'environnement virtuel existant..."; \
		rm -rf .venv; \
		echo "L'ancien environnement a été supprimé."; \
	fi

	@echo "Création d'un nouvel environnement Python 3.12..."
	python3.13 -m venv .venv
	@echo "Activation de l'environnement et installation des dépendances..."
	. .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt
	@echo "✅ Installation terminée avec succès!"
.PHONY: install

upgrade: ## Mise à jour des dépendances
	
.PHONY: upgrade


clean: ## Nettoyage des fichiers temporaires
	rm -rf __pycache__
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -f *.egg-info
.PHONY: clean