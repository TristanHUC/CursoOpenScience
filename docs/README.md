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
- Install the grobit container, following their documentation : https://grobid.readthedocs.io/en/latest/Grobid-docker/
1) pull the docker image of grobid :  docker pull lfoppiano/grobid:latest-develop
2) run the docker image : docker run -p 8070:8070 lfoppiano/grobid:latest-develop


# How to execute
- put your pdf in the host_volume/dataset folder
- run the script_grobid_pdf
- Now your files should have been processed, make sure they are by checking the grobid_output directory.
- build the docker image :  docker build --no-cache -t test .
- run the docker image : docker run -it -v C:\Users\trist\UTC\curso_de_Inteligienca_artificial_y_cienca_abierta\grobid\host_volume:/volume test
- Then in the container, you can run any of the 3 scripts : script_wordcloud, script_list_link or script_visualization and the result we appear in the host_volume/output directory
- For script_wordcloud and script_list_link you have to run with the name of your pdf in parameter. For example : poetry run python ../work/script_wordcloud.py exemple_pdf10.pdf
- For the script_visualization : no argument needed just run : poetry run python ../work/script_visualization.py

  Author : Tristan Hucher
  Mail : tristan.hucher@gmail.com

# Documentation

See all documentation at https://curso-open-science-v2.readthedocs.io/en/latest/

[![DOI](https://zenodo.org/badge/753142842.svg)](https://zenodo.org/doi/10.5281/zenodo.10712488)
