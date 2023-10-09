# **Configuration de l'environnement virtuel avec pyenv-win**

Ce projet utilise pyenv-win pour gérer l'environnement virtuel et les dépendances.
## Installation de pyenv-win
Vous devez installer pyenv-win afin de créer un environnement virtuel qui supportera les dépendances.

[**Lien vers le Github de pyenv-win**](https://github.com/pyenv-win/pyenv-win)
## Installation des dépendances

Pour installer les dépendances nécessaires, exécutez la commande suivante :

`pip install -r .\requirements.txt`

Cette commande installera les librairies spécifiées dans le fichier requirements.txt dans votre environnement virtuel.

# **Démarrage de l'environnement virtuel**
Pour démarrer l'environnement virtuel, exécutez la commande suivante :

`.\.venv\Scripts\activate`

Cette commande activera l'environnement virtuel, vous permettant d'exécuter le code avec les dépendances spécifiées localement.

## Sélection de l'interpréteur virtuel Python
Assurez-vous d'avoir l'interpréteur virtuel Python sélectionné après avoir activé l'environnement virtuel. Vous pouvez vérifier l'interpréteur Python en utilisant la commande sur Visual Studio Code:

`>Python: Select Interpeter`

# **Exécution du code**
Vous pouvez maintenant exécuter `app.py` ou `test_app.py` dans votre IDE avec votre environnement virtuel configuré et les dépendances installés.
