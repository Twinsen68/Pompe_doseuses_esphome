# Pompe Doseuses ESPHome

Ce projet fournit une configuration ESPHome pour contrôler **4 pompes doseuses** utilisant des moteurs pas à pas **28BYJ-48** (5V) pilotés par des drivers **ULN2003**. La solution permet d’activer chaque pompe via Home Assistant grâce à des switches template.

## Fonctionnalités

- **Contrôle de 4 pompes doseuses :**
  Chaque pompe est associée à un moteur 28BYJ-48 et un driver ULN2003.
- **Séquence de pas intégrée :**
  Exécution d'une séquence de 8 demi-pas pour piloter les moteurs (512 demi-pas par défaut, ajustable).
- **Activation via Home Assistant :**
  Utilisation de switches template pour déclencher manuellement les scripts de contrôle.
- **Configuration flexible :**
  Possibilité d’ajuster les pins, le nombre de pas et les délais selon vos besoins.

## Matériel Requis

- Carte ESP32 (ou ESP8266 compatible avec ESPHome)
- 4 moteurs pas à pas **28BYJ-48** (5V)
- 4 drivers **ULN2003**
- Alimentation 5V adaptée aux moteurs
- Câblage et connecteurs

## Installation

1. **Copiez le contenu du fichier `install.yaml` :**  
   Ouvrez le fichier `install.yaml` du projet et copiez son contenu dans votre configuration ESPHome.
2. **Ouvrir le projet dans ESPHome :**  
   Chargez le fichier copié dans ESPHome.
3. **Configurer le fichier :**  
   Adaptez les pins et autres paramètres selon votre câblage.
4. **Compiler et téléverser :**  
   Compilez la configuration et téléversez-la sur votre carte via ESPHome.
5. **Intégrer dans Home Assistant :**  
   Ajoutez l’appareil via l’API ESPHome pour contrôler les pompes à distance.

## Configuration

Le fichier de configuration inclut :

- **Substitutions :**
  Définition des pins pour chaque bobine des moteurs.
- **Déclaration des sorties GPIO :**
  Configuration des sorties pour piloter les bobines.
- **Scripts de contrôle :**
  Chaque script exécute la séquence de 8 demi-pas pour actionner le moteur (avec 512 demi-pas par défaut).
- **Switches Template :**
  Permettent de lancer les scripts via Home Assistant.

> **Attention :**
> La boucle avec `delay()` dans les scripts peut bloquer temporairement l’exécution d’ESPHome. Pour une utilisation en production, envisagez une approche non bloquante (par exemple, via des timers ou un composant personnalisé).

## Utilisation

- **Activation d'une pompe :**
  Depuis Home Assistant, activez le switch correspondant (ex. "Activer Pompe 1") pour lancer le script associé.
- **Personnalisation :**
  Modifiez le nombre de pas, les délais ou la séquence des demi-pas pour adapter le comportement du moteur à vos besoins.

## Contributions

Les contributions et suggestions sont les bienvenues !
Pour proposer des améliorations, ouvrez une [issue](https://github.com/Twinsen68/Pompe_doseuses_esphome/issues) ou soumettez une pull request.

## License

Ce projet est distribué sous la licence [MIT](LICENSE).
