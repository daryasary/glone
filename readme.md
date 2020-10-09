# Gitlab project cloner

## Instructions

* Get your gitlab token
* Install pip and virtualenv
    `sudo apt install python3-pip python3-virtualenv`
    
* Create virtualenv
    `virtualenv -p python3 ven`
   
* Clone Glone project
    `git clone https://github.com/daryasary/glone.git glone`
* Activate virtualenv
    `source venv/bin/activate`
    
* Go to project directory and install requirements
    ```
    cd glone
    pip install -r requirements.txt
  ```
* Run Glone
    ```
    python main.py -t <token> -g <gitlab-group-id>  # get specific git group prjects
    python main.py -t <token> -u <your-gitlab-username>  # get specific gitlab user prjects
    python main.py -t <token> -u <your-gitlab-username> -g <gitlab-group-id>  # get both user and group projects
  ```
 then all projects will be cloned into `projects` directory