import inquirer
import os
def ask_questions():
    global answers
    questions = [
        # title of repository
        inquirer.Text('title', message="What's the title of your repository?"),
        # description of repository
        inquirer.Text('description', message="What's the description of your repository?"),
        # language of repository
        inquirer.Text('language', message="What's the language of your repository?"),
        # language badge url 
        inquirer.Text('language_badge_url', message="What's the language badge url of your repository?"),
        # repository url
        inquirer.Text('repository_url', message="What's the repository url of your repository?"),
        #install instructions
        inquirer.Editor('install_instructions', message="What's the install instructions of your repository?"),
        #usage instructions
        inquirer.Editor('usage_instructions', message="What's the usage instructions of your repository?"),
        #screenshots
        inquirer.Editor('screenshots', message="What's the screenshots of your repository?"),
        # license
        # checkbox 
        inquirer.Checkbox('license', message="What's the license of your repository?", choices=[
                "None",
                "Apache2.0",
                "GNU Public v3.0",
                "MIT",
                "Boost Software 1.0",
                "Creative Commons Zero v1.0 Universal",
                "Eclipse Public 2.0",
                "GNU Affero General Public v3.0",
                "GNU General Public v2.0",
                "GNU Lesser General Public v2.1",
                "Mozilla Public 2.0",
                "the Unilicense"
                ], carousel=True
            ),
        # license year
        inquirer.Text('license_year', message="What's the license year of your repository?"),
        # directory of readme
        inquirer.Text('directory_of_readme', message="What's the directory of readme of your repository?"),
    ]

    answers = inquirer.prompt(questions)
    if answers['directory_of_readme'] == '':
        answers['directory_of_readme'] = os.getcwd()
    answers['screenshots'] = answers['screenshots'].splitlines()
    for i in range(len(answers['screenshots'])):
        answers['screenshots'][i] = '<a><img src ="'+answers['screenshots'][i]+'" alt ="Screenshot"/></a>'
    answers['screenshots'] = '\n'.join(answers['screenshots'])
def create_readme():
    file_path = answers['directory_of_readme']+'/README.md'
    with open(file_path, 'w') as f:
        a = '''<h1 align="center">{}</h1>
    <div align = "center">
    <a>
    <img src ="{}" alt ="{}"/>
    </a>
    </div>
    <p align = "center">
<a href = 'https://code.visualstudio.com/'>
    <img alt ='Visual Studio Code' src='https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg'/>
    </a>
    <a href="{}" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
</a>
<a href="{}"><img src="https://img.shields.io/badge/License-{}-brightgreen.svg"></a>  
<a href="https://twitter.com/BholaJaivardhan" target="_blank">
<img alt="Twitter: BholaJaivardhan" src="https://img.shields.io/twitter/follow/BholaJaivardhan.svg?style=social" />
</a>
</p>

# Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [About the author](#about-the-author)
- [Contribution](#contribution)
- [Support Us](#show-your-support)
- [License](#license)

# Description
> {}

# Installation
{}

# Usage
{}

# Screenshots
{}

# About-the-author
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jaivardhan-bhola)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/jaivardhan-bhola-773944214)
[![Twitter](https://img.shields.io/badge/BholaJaivardhan-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/BholaJaivardhan)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jaivardhan.bhola@gmail.com)

# Contribution
If you would like to contribute to this project reach out to me. Contact Information can be found below or by clicking on the 'Contact-Information' link provided in the Table of Contents.

# Show-your-support
Give a ⭐️ star if this project helped you!

# License
Copyright © {} [Jaivardhan Bhola](https://github.com/jaivardhan-bhola).<br />
This project is [{}]({}) licensed.
***
<div align = "center"><img src="https://madewithlove.now.sh/in?heart=true&colorA=%23505050&colorB=%235032b4&template=for-the-badge&text=India" alt="Made with love in India"></div>

    '''.format(answers['title'], answers['language_badge_url'], answers['language'], answers['repository_url'], answers['repository_url']+'/blob/main/LICENSE', answers['license'][0], answers['description'], answers['install_instructions'], answers['usage_instructions'], answers['screenshots'], answers['license_year'], answers['license'][0], answers['repository_url']+'/blob/main/LICENSE')
        f.write(a)
def main():
    print("Welcome to the README.md generator")
    ask_questions()
    create_readme()
    print("README.md created successfully")

main()