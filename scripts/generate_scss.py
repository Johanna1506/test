import csv
import os

def generate_base_scss():
    # Styles généraux
    base_scss_content = """// Styles de base de la page des projets
.top_text_zone {
  background-color: var(--color-highlight);
  height: 260px;
  color: var(--color-primary);
  display: flex;
  align-items: center;
  justify-content: center;

  h1 {
    font-size: 2.2em;
    text-align: center;
    font-weight: bold !important;
    text-transform: none !important;
  }
}

.boxslider {
  background-color: var(--color-background) !important;
}

#section_own_projects {
  > .grid {
    margin: 0 !important;
    display: flex !important;
    gap: 12px !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: center !important;

    > .grid__item {
      padding: 0 !important;
      width: auto !important;
    }
  }
}

#projects_discover_section_explore {
  display: none !important;
}

#projects_section_explore {
  > .eight-tenths {
    width: 100% !important;
  }
}

@media screen and (max-width: 600px) {
  #section_own_projects {
    > .grid {
      flex-direction: column !important;
      align-items: center !important;
    }
  }
}

// Masquer tous les projets par défaut
[id^="box_project_"] {
  display: none !important;
}
"""
    # Écrire le fichier de styles de base
    with open('scss/_projects-page-base.scss', 'w') as f:
        f.write(base_scss_content)

def generate_user_rules_scss():
    # Lire le CSV
    user_projects = {}
    with open('csv/clubdeal.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row['userid']
            project_id = row['projectid']
            if user_id not in user_projects:
                user_projects[user_id] = []
            user_projects[user_id].append(project_id)

    # Générer le SCSS pour les règles utilisateur
    rules_scss_content = """// Règles de visibilité des projets par utilisateur
// Ce fichier est généré automatiquement, ne pas modifier manuellement
"""
    # Ajouter les règles pour chaque utilisateur
    for user_id, project_ids in user_projects.items():
        rules_scss_content += f"""
// Afficher les projets pour l'utilisateur {user_id}
body:has(#desktop_default_client_space[href="/fr/users/{user_id}/edit"]) {{
"""
        for project_id in project_ids:
            rules_scss_content += f"  #box_project_{project_id} {{\n"
            rules_scss_content += "    display: block !important;\n"
            rules_scss_content += "  }\n"
        rules_scss_content += "}\n"

    # Écrire le fichier de règles utilisateur
    with open('scss/_projects-page-rules.scss', 'w') as f:
        f.write(rules_scss_content)

def generate_scss():
    generate_base_scss()
    generate_user_rules_scss()

if __name__ == "__main__":
    generate_scss()