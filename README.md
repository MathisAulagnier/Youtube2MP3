# Convertisseur Youtube vers MP3/MP4

Ce script Python vous permet de télécharger du contenu audio (webm) ou vidéo (MP4) depuis YouTube en utilisant la bibliothèque Pytube. Vous pouvez spécifier l'URL de la vidéo YouTube que vous souhaitez télécharger ainsi que le format de téléchargement.


## Utilisation

Pour utiliser ce script, suivez les étapes suivantes :

1. Assurez-vous d'avoir [Python](https://www.python.org) installé sur votre système.

2. Installez la bibliothèque `pytube` si elle n'est pas déjà installée en utilisant la commande suivante :

   ```bash
   pip install pytube
   ```

3. Exécutez le script en spécifiant les paramètres d'entrée suivants :

`--url : L'URL de la vidéo YouTube que vous souhaitez télécharger.(String)`

`--f : Le format de téléchargement.(String)`


Voici un exemple d'utilisation :

```bash
# Télécharge uniquement le son : 
python3 youtube_downloader.py --url 'URLVideoYoutube'
# Télécharge la vidéo en MP4 :
python3 youtube_downloader.py --url 'URLVideoYoutube' --f 'V'
```

Le/La Son/Vidéo télécharger sera enregistré sous le nom de la vodéo et dans le répertoire actuel.

Configuration par défaut

Si vous ne spécifiez pas d'arguments, le script utilisera les valeurs par défaut suivantes :
URL : "https://www.youtube.com/watch?v=Cp9pk-FkE6E"
Format : 'M' -> pour uniquement le son

## Remarque

Si vous spécifiez un format non pris en charge, le script affichera un message d'erreur.
Les formats pris en compte sont :
- [`music` ; `Music` ;`musique` ; `Musique` ; `m` ; `M`] pour télécharger un fichier son.
- [`video` ; `Video` ; `v` ; `V`] pour télécharger un fichier vidéo.


## Auteur

Ce script a été créé par Aulagnier Mathis.

## Licence

Ce script est sous licence MIT. Consultez le fichier [LICENSE](LICENSE.md) pour plus de détails.