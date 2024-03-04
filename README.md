## Project of curso_open_science
# Composition
This repository is composed of 4 scripts :
- script_grobid_pdf you should run first to process your pdf which should be in dataset to TEI format so it can be process by other script.
- script_wordcloud allows you to draw a wordcloud from the most represented words in the abstract of your paper.
- script_visualization allows you to draw a visualization of the number of figure in each papers of your dataset.
- script_list_link allows you to print a list of all links present in your paper.

# Requirement 
- The requirement to run the project could be found in requirements.txt or in the pyproject.toml

# How to install 
- clone the repository 
- do a poetry install
- put your pdf in the dataset folder
- run the script ... (script pour lancer docker et le container)
- run the script_grobit_pdf.py 
- you can now run any script you want

# How to execute
- Put your pdf in the dataset part
- run the script_grobid_pdf
- Now your files should have been processed, make sure they are by checking the output directory.
- Then you can run any of the 3 scripts : script_wordcloud, script_list_link or script_visualization.
- For script_wordcloud and script_list_link you have to run with the name of your pdf in parameter. For exemple script_wordcloud exemple_pdf10.pdf

  Author : Tristan Hucher
  Mail : tristan.hucher@gmail.com

[![DOI](https://zenodo.org/badge/753142842.svg)](https://zenodo.org/doi/10.5281/zenodo.10712488)
