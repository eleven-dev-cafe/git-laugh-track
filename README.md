# 📢 Git Laugh Track 🎶

![GitHub stars](https://img.shields.io/github/stars/eleven-dev-cafe/git-laugh-track?style=social)
![GitHub forks](https://img.shields.io/github/forks/eleven-dev-cafe/git-laugh-track?style=social)
[![License: BSD-3](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/eleven-dev-cafe/.github/blob/main/CONTRIBUTING.md)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

***Play funny sound effects on every **Git commit** or **push**.***  
***Turn boring commits into a party 🎉***

</br>

## ✨ Features
- 🔊 Play a random `.mp3` from your sound library on **commit** and **push**  
- ⚡ Works across **Linux, macOS, Windows (via WSL/terminal)**  
- 🎛 CLI commands to **play**, **add**, and **list** sounds  
- 🔗 Easy setup via global Git hooks

</br>

## 🗺️ Architecture

```mermaid
flowchart TD
    User["👤 User (Developer)"]
    Git["🐙 Git Client"]
    PostCommitHook["🔗 post-commit Hook (hooks/post-commit)"]
    SoundFiles["🎵 Sitcom Laugh Tracks (~/.git-laugh-sounds/*.mp3)"]
    AudioPlayer["🎧 Audio Player (playsound, mpg123, afplay)"]
    Installer["⚡ global-install.sh"]
    Uninstaller["🗑️ uninstall.sh"]

    User --makes commit--> Git
    Git --triggers--> PostCommitHook
    PostCommitHook --selects random mp3--> SoundFiles
    PostCommitHook --calls--> AudioPlayer
    Installer --sets up hooks & sounds--> PostCommitHook
    Installer --copies--> SoundFiles
    Uninstaller --removes--> PostCommitHook
    Uninstaller --removes--> SoundFiles
```

</br>

## 🎥 Demo Video(Enable Sound 🔊) 
https://github.com/user-attachments/assets/794d3f7e-eace-496e-8534-2134725aa4d6  

</br>

## 📦 Installation

Clone the repo and install it locally:

```bash
git clone https://github.com/eleven-dev-cafe/git-laugh-track.git
cd git-laugh-track
pip install .
```
This installs the CLI command git-laugh.

</br>

### 🎮 Usage

**Once installed, you can use the CLI tool:**

Setup Git hooks and sounds for laugh sounds
```bash
git-laugh install       
```

Remove Git hooks and Sounds
```bash
git-laugh uninstall
```

Play a random laugh sound on each commit..
```bash
git-laugh play 
```

### Git workflow
- Run `git commit -m "fix bug"` → plays a random sound 🎶
- Run `git push` → plays another random sound 


</br>

### 🔊 Adding Sounds

Place `.mp3` files into your sound directory:
- Default: `~/.git-laugh-sounds/`
Or add via CLI:
```bash
git-laugh add funny.mp3
```
> Reinstall `git-laugh` to copy sounds at defaults

</br>

## 🛠 Development

Install dev dependencies:
```bash
pip install -r requirements.txt
```

Run tests:
```bash
pytest
```

</br>
## 📜 License

This project is licensed under the `BSD 3-Clause` License – see the [LICENSE](LICENSE) file for details.

</br>

## 👨‍💻 Developer  
`Gyarsilal Solanki`

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230A66C2.svg?logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/gyarsilal-solanki)  🤝  [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/gyarsilalsolanki011)

  
Join us to discuss ideas, share feedback, and coordinate contributions:  
[![Join Discord](https://img.shields.io/discord/1405808666179014697?color=4CBB17&label=Join%20Us%20on%20Discord&logo=discord&logoColor=blue)](https://discord.gg/Zrc9x3ts)

</br>

## 💡 Inspiration

**Because coding is serious business… but your commits don’t have to be 🤣**</br>
***If you find this project helpful, consider giving it a ⭐ to support!***
