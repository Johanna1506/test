# Prosperia Website

## Gestion des projets visibles par utilisateur

Le système utilise un fichier CSV pour gérer quels projets sont visibles pour quels utilisateurs.

### Structure du CSV

Le fichier `csv/clubdeal.csv` doit suivre ce format :

```csv
userid,projectid
34771,406953
34772,406953
```

- `userid` : L'ID de l'utilisateur
- `projectid` : L'ID du projet à afficher pour cet utilisateur

### Compilation du SCSS

Pour compiler le SCSS avec les règles de visibilité des projets :

```bash
# En mode développement (avec watch)
npm run sass

# Pour la production
npm run sass:build
```

Le processus de compilation :

1. Génère le SCSS à partir du CSV
2. Compile le SCSS en CSS

### Mise à jour des règles de visibilité

Pour mettre à jour les règles de visibilité :

1. Modifier le fichier `csv/clubdeal.csv`
2. Relancer la compilation avec `npm run sass` ou `npm run sass:build`
