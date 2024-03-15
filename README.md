# Project Name
Data Analysis on Dataset using Docker and Docker Contaniner
## Overview
This project aims to make preprocessing for dataset and make a visulaization on it and apply k means model inside docker contanier and then get the output of each file in our local machine 

## Prerequisites
- Docker installed on your machine.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory name as (bd-a1).
3. Build the Docker image:
    ```bash
    docker build -t bd-a1-image .
    ```
4. Run the Docker container:
    ```bash
    docker run -it --name bd-a1-container bd-a1-image
    ```
5. Now inside the container i make directory name /home/doc-bd-a1/ 
    ```bash
    cd  /home/doc-bd-a1/
    ```
6. First , I do the python file 
   ```bash
   touch load.py dpre.py eda.py model.py vis.py
   ```
7. Second, I go to each file by using  nano command such as 
   ```bash
   nano load.py
   ```
8. Third , I write in each file the python code when the bash open 
9. Fourth , I run each file by using 
   ```bash
   python3 <File name> </path/to/dataset>
   ```
10. End , After i run the all files I use this command to list for me the files inside this directory 
    ```bash
    ls
    ```
11. This command for get out of the directory 
    ```bash
    cd ..
    ```
12. Exit the contanier by using 
     ```bash
    exit
    ```
13. The command to start the container after exit it 
    ```bash
    docker start -i bd-a1-container #### replace bd-a1-container by your container name 
    ```
14. To run the bash script file using this command to get the output files from the contanier to local machine
     ```bash
    bash final.sh
    ### another one
    chmod +x final.sh
    ./final.sh
    ```

## Project Structure

- `Dockerfile`: Contains instructions to build the Docker image.
- `load.py`: Python script to initiate the pipeline and process the dataset.
- `dpre.py`: Python script responsible for data preprocessing steps such as cleaning, transformation, reduction, and discretization.
- `eda.py`: Python script for exploratory data analysis, generating insights from the dataset.
- `vis.py`: Python script for data visualization, creating plots and charts to visualize the data.
- `final.sh`: Bash script for orchestrating the entire pipeline, including Docker container setup, data processing, and result retrieval.

### File Descriptions

#### Dockerfile
This file contains instructions to build a Docker image containing all dependencies required to run the project. It installs necessary packages and sets up the environment.

#### load.py
The `load.py` script serves as the entry point for the pipeline. It loads the dataset, invokes subsequent Python scripts for data processing, and initiates the pipeline.

#### dpre.py
The `dpre.py` script is responsible for performing data preprocessing steps such as cleaning, transformation, reduction, and discretization. It reads the dataset, applies preprocessing techniques, and saves the processed data.

#### eda.py
The `eda.py` script conducts exploratory data analysis (EDA) on the dataset. It generates insights, statistics, and visualizations to understand the data distribution, relationships, and patterns.

#### vis.py
The `vis.py` script handles data visualization tasks. It creates plots, charts, and graphs to visualize the data distribution, trends, and correlations.

## `final.sh`

This script is used to retrieve the processed data and results from the Docker container after running the data processing pipeline.

### Commands Explanation:

1. `docker cp 767889e80e7e:/home/doc-bd-a1/res_dpre.csv service-result/`: Copies the processed data file `res_dpre.csv` from the Docker container to the `service-result` directory on the local machine.

2. `docker cp 767889e80e7e:/home/doc-bd-a1/eda-in-1.txt service-result/`: Copies the first insight file `eda-in-1.txt` from the Docker container to the `service-result` directory on the local machine.

3. `docker cp 767889e80e7e:/home/doc-bd-a1/eda-in-2.txt service-result/`: Copies the second insight file `eda-in-2.txt` from the Docker container to the `service-result` directory on the local machine.

4. `docker cp 767889e80e7e:/home/doc-bd-a1/eda-in-3.txt service-result/`: Copies the third insight file `eda-in-3.txt` from the Docker container to the `service-result` directory on the local machine.

5. `docker cp 767889e80e7e:/home/doc-bd-a1/vis.png service-result/`: Copies any visualization file `vis.png` from the Docker container to the `service-result` directory on the local machine.

6. `docker cp 767889e80e7e:/home/doc-bd-a1/k.txt service-result/`: Copies any additional files, such as logs or notes, named `k.txt` from the Docker container to the `service-result` directory on the local machine.

**Note:** Make sure to replace `767889e80e7e` with the actual container ID or name, and `service-result` with the appropriate directory path where you want to save the files on the local machine.



## Pipeline Execution
1. The `load.py` script reads the dataset from the specified path and initiates the pipeline.
2. Each Python file in the pipeline processes the data frame and invokes the next Python file.
3. Data frames are passed between Python files for further processing.
4. Various files and figures are generated as outputs during the pipeline execution.

## Output Files

- `res_dpre.csv`: Processed dataset after data preprocessing.
- `eda-in-1.txt`, `eda-in-2.txt`, `eda-in-3.txt`: Insight files generated during exploratory data analysis.
- `vis.png`: Visualization output file, if applicable.
- `k.txt`: Additional output file containing logs or notes, if generated during the data processing pipeline


## Notes
- Make sure to replace `/path/to/dataset` with the actual path to your dataset.
- Additional instructions or notes can be added here.
-  Docker Image on Docker Hub Link :https://hub.docker.com/layers/tokanabil/my_repository/latest/images/sha256-ba828520c94aa2c5870c9b9de949f9d977435cb9a3fbdec0105fe4ed18e37b96?context=explore 


