// function to generate markdown for README
function generateMarkdown(data) {
  // returns inquirer prompted data. Writing in markdown inside backticks and using data to personalize markdown page.
  return `<h1 align="center">${data.title}</h1>
  <div align = "center">
  <a>
  <img src =${data.language} alt ="Python"/>
    </a>
    </div>
  <p align = "center">
<a href = 'https://code.visualstudio.com/'>
  <img alt ='Visual Studio Code' src='https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg'/>
  </a>
  <a href="${data.repo}" target="_blank">
  <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
</a>
<a href="${data.licenseUrl}"><img src="https://img.shields.io/badge/License-${data.license[0]}-brightgreen.svg"></a>  
<a href="https://twitter.com/BholaJaivardhan" target="_blank">
<img alt="Twitter: BholaJaivardhan" src="https://img.shields.io/twitter/follow/BholaJaivardhan.svg?style=social" />
</a>
</p>

# Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [About the author](#about-the-author)
- [Contribution](#contribution)
- [Support Us](#show-your-support)
- [License](#license)

# Description
> ${data.description}

# Installation
${data.installation}

# Usage
${data.usage}

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
Copyright © ${data.licenseYear} [Jaivardhan Bhola](https://github.com/jaivardhan-bhola).<br />
This project is [${data.license}](${data.licenseUrl}) licensed.
***
<div align = "center"><img src="https://madewithlove.now.sh/in?heart=true&colorA=%23505050&colorB=%235032b4&template=for-the-badge&text=India" alt="Made with love in India"></div>

`;
}
// function exportying generateMarkdown function
module.exports = generateMarkdown;
