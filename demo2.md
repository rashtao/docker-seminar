
1. build an image
    
    ```bash
    git clone git@github.com:rashtao/docker-seminar.git
    cd docker-seminar
    docker build -t easter-calculator:dev .
    ```

2. run it

    ```bash
    docker run -t -d --name easter-calculator easter-calculator:dev
    docker logs -f easter-calculator
    ```

3. run with params 

    ```bash
    docker run -it --rm easter-calculator:dev ./main.py a b c
    ```

4. run with envars 

    ```bash
    docker run -it --rm -e MYVAR=yoyo easter-calculator:dev env
    ```

5. Create an account at [https://hub.docker.com](https://hub.docker.com) and login into it:

    ```bash
    export DOCKER_USER=<yourDockerHubUserName>    
    docker login --username=${DOCKER_USER}
    ```

6. tag & push

    ```bash
    docker tag easter-calculator:dev docker.io/${DOCKER_USER}/easter-calculator:1.0
    docker push docker.io/${DOCKER_USER}/easter-calculator:1.0
    ```

7. check the image at [https://hub.docker.com/u/<yourDockerHubUserName>](https://hub.docker.com/u/<yourDockerHubUserName>)

8. to run the image in another machine:

    ```bash
    docker run -it --name easter-calculator docker.io/${DOCKER_USER}/easter-calculator:1.0
    ```
