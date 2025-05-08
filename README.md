<h1 align="center" style="color:#00BFFF;">🛡️ Xiwa - Advanced System Info & Secure Dispatch</h1>

<p align="center" style="color:white;">
Un outil de récupération d'infos système complet et ultra-sécurisé, avec envoi automatisé vers Discord via Webhook.
</p>

<br>

<div align="center">

<a href="#🚀-introduction">
  <img src="https://img.shields.io/badge/🚀_Intro-000?style=for-the-badge&logo=python&logoColor=white&color=000000&labelColor=00BFFF" />
</a>
<a href="#📦-installation">
  <img src="https://img.shields.io/badge/📦_Installation-000?style=for-the-badge&logo=windows&logoColor=white&color=000000&labelColor=00BFFF" />
</a>
<a href="#⚙️-configuration">
  <img src="https://img.shields.io/badge/⚙️_Webhook-000?style=for-the-badge&logo=discord&logoColor=white&color=000000&labelColor=00BFFF" />
</a>
<a href="#🔧-fonctions">
  <img src="https://img.shields.io/badge/🔧_Fonctions-000?style=for-the-badge&logo=gear&logoColor=white&color=000000&labelColor=00BFFF" />
</a>

</div>

---

## 🚀 Introduction

> **Xiwa** est un script Python puissant qui :
> - Installe automatiquement les dépendances nécessaires.
> - Récupère toutes les infos critiques de votre système (OS, RAM, CPU, GPU, etc.).
> - Envoie ces données formatées directement sur un serveur Discord via **Webhook**.
> - Peut être étendu pour du VPN ou autre anonymisation.

---

## 📦 Installation

### 1. Cloner le projet

```bash
# 1. Cloner le dépôt Git

git clone https://github.com/ton-utilisateur/xiwa.git
cd xiwa

# 2. Créer un environnement virtuel (optionnel mais recommandé)

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Lancer le script

python main.py
```

---

## ⚙️ Configuration

### 🔗 Webhook Discord

Dans le fichier `simplifier.py`, recherchez la ligne contenant :

```python
# YOUR WEBHOOK
```

Et remplacez-la par :

```python
w3bh00k = SyncWebhook.from_url("https://discord.com/api/webhooks/...")
```

---

## 🔧 Fonctions disponibles

| Fonction       | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `systemInfo()` | Récupère les infos système et les envoie à Discord           |
| `vp1()`        | Active un VPN sécurisé (simulation ou implémentation réelle) |
| `h3llo()`      | Fonction test pour afficher un message de bienvenue          |

---

## 🧠 Bibliothèques utilisées

* `psutil`
* `platform`
* `colorama`
* `discord`
* `requests`
* `pathlib`
* et d'autres selon les besoins du projet

> ⚠️ L'installation automatique des bibliothèques nécessaires est intégrée au script si besoin.

---

## 📂 Exemple d'importation

```python
from path.to.simplifier import *
```

---

## 📸 Aperçu du script

```html
<img src="img/readme-img-simplifier.PNG" alt="Aperçu du script" style="border:2px solid #00BFFF; border-radius:10px;" />
```

---

## ⚠️ Disclaimer

Ce projet est à **usage personnel uniquement**. Toute utilisation d’un webhook Discord pour recevoir des données doit se faire **avec le consentement explicite** de l’utilisateur concerné et en **conformité avec les lois sur la confidentialité** des données.

---

## 🔐 Sécurité

* ✅ Installation des paquets sous surveillance
* ✅ Transmission sécurisée via HTTPS (webhook Discord)
* ✅ Code clair et facile à auditer

---

<div align="center">
  <h3 style="color:#00BFFF;">© 2025 Dryz3R — All Rights Reserved</h3>
</div>
