# WEBSOCKET

# Process Execution
## Local

#### Environment
    conda create -n websocket python=3.7
    conda activate websocket
    uvicorn example:app

#### Run 
    gtoken=`gcloud auth print-identity-token` && python main.py --mode test --version "0.0.0" --token $gtoken --model-version "0.0.0"

## Docker 

#### Build
    sudo docker build . -t websocket

#### Run
    sudo docker run -it -e PORT=9191 websocket