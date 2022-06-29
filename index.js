const inquirer = require("inquirer");
const fs = require("fs");
const path = require("path");
var generateMarkdown = require("./generateMarkdown");
    
function writeToFile(fileName, data) {
  fs.writeFileSync(path.join(process.cwd(), fileName), data);
}

function init() {
  inquirer.prompt([
    {
      type: "input",
      name: "title",
      message: "What's Your Project's Name?"
      },
      {
        type: "input",
        name: "description",
        message: "Enter A Descrition For Your Project"
      },
      {
        type: "input",
        name: "repo",
        message: "Enter Repository Link"
      },      
      {
        type: "editor",
        name: "installation",
        message: "Enter Your Project's Installation Instructions"
      },
      {
        type: "editor",
        name: "usage",
        message: "Enter Usage Info"
      },
      { 
          type: "checkbox",
          message: "Licensing Options",
          name: "license",
          choices: [
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
            ]
        },
        {
            type: "input",
            name: "licenseUrl",
            message: "Enter license URL"
        },
        {
            type: "input",
            name: "licenseYear",
            message: "Enter licensing year"
        },
        {
          type: "input",
          name: "language",
          message: "Enter language badge URL"
        }        
    ]).then(function(data) {
      console.log("Generated Markdown In Source Directory");
      writeToFile("README.md", generateMarkdown({...data}));  
});
}
init()