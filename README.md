# 📢 Git Laugh Track 🎶

![GitHub stars](https://img.shields.io/github/stars/eleven-dev-cafe/git-laugh-track?style=social)
![GitHub forks](https://img.shields.io/github/forks/eleven-dev-cafe/git-laugh-track?style=social)
[![License: BSD-3](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/eleven-dev-cafe/.github/blob/main/CONTRIBUTING.md)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

> Play funny sound effects on every **Git commit** or **push**.  
> Turn boring commits into a party 🎉

</br>

## ✨ Features
- 🔊 Play a random `.mp3` from your sound library on **commit** and **push**  
- ⚡ Works across **Linux, macOS, Windows (via WSL/terminal)**  
- 🎛 CLI commands to **play**, **add**, and **list** sounds  
- 🔗 Easy setup via global Git hooks  

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

## ⚙️ Setup Git Hooks
Install globally so all repos get the funny sounds:
```bash
./scripts/global-install.sh
```

Uninstall later if you want:
```bash
./scripts/uninstall.sh
```
</br>

## 🎮 Usage

Once installed, you can use the CLI tool:
```bash
git-laugh install   # Setup Git hooks for laugh sounds
git-laugh uninstall # Remove Git hooks
git-laugh play      # Play a random laugh sound manually
```
</br>

### Git workflow

- Run `git commit -m "fix bug"` → plays a random sound 🎶
- Run `git push` → plays another random sound 🎶

## 🔊 Adding Sounds

Place `.mp3` files into your sound directory:
- Default: `~/.git-laugh-sounds/`
Or add via CLI:
```bash
git-laugh add funny.mp3
```

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

## 👨‍💻 Maintainer  
`Gyarsilal Solanki`

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230A66C2.svg?logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/gyarsilal-solanki)  🤝  [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](https://github.com/gyarsilalsolanki011)

  
Join us to discuss ideas, share feedback, and coordinate contributions:  
[![Join Discord](https://img.shields.io/discord/1405808666179014697?color=4CBB17&label=Join%20Us%20on%20Discord&logo=discord&logoColor=blue)](https://discord.gg/Zrc9x3ts)

</br>

## 📜 License

This project is licensed under the `BSD 3-Clause` License – see the [LICENSE](LICENSE) file for details.


## 💡 Inspiration

**Because coding is serious business… but your commits don’t have to be 🤣**
