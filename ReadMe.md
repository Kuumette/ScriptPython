# Last Image

## Modification des niveaux de l'image et transformation en PNG

Utilisation de python

```
$ python fitsToPngNiveaux.py
```

## Transformer l'image en JPG

Utilisation de la CLI imageMagick. Ce placer dans le dossier ou se trouver les images à transformer

```
$ magick \*.png a.jpg
```

# Last Substraction Image

La soustraction de 2 images ce fais en fits

-   $ python soustraction.py

-   Faire la procedure de last Image

# Video

-   Mettre les images en JPG de la video dans un fichier sépare

-   Redimensionner les image

```
$ python resize.py

$ python video.py
```

# Overlay / TCS

```
$ magick -size 4096x4096 xc:transparent transparent.png

$ python overlay.py
```
