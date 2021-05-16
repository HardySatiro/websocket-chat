# WEBSOCKET

# Process Execution
## Local

#### Environment
    conda create -n websocket python=3.9
    conda activate websocket
    pip install -r requirements.txt

#### Run 
    uvicorn wsgi:app --host "0.0.0.0" --port 9191 --workers 1 --reload

## Docker 

#### Build
    sudo docker build . -t websocket

#### Run
    sudo docker run -it -e PORT=9191 websocket