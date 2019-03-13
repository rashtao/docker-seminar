
1. Run a container

    ```bash
    sudo docker run --name hello-world hello-world
    ```

2. List local images

    ```bash
    sudo docker images
    ```

3. Run an interactive container 
    ```bash
    sudo docker run -it --name ubuntu ubuntu bash
    ```
    
    Run in the container and in the host:
    ```bash
    cat /etc/issue
    ps aux
    uname -a
    ```

4. List containers
    ```bash
    sudo docker ps
    sudo docker ps -a
    ```

5. Show logs
    ```bash
    sudo docker logs hello-world
    sudo docker logs ubuntu
    ```

6. Show stats
    ```bash
    sudo docker stats ubuntu
    ```

7. Start / Stop / Restart
    ```bash
    sudo docker start hello-world
    sudo docker stop ubuntu
    ```

8. Run in background
    ```bash
    sudo docker run -it -d --name ubuntu-top ubuntu top
    ```

9. docker exec
    ```bash
    sudo docker exec -it ubuntu-top bash
    ps aux
    ```

10. mount a volume
    ```bash
    # in the host
    mkdir /tmp/docker-data
    echo "Hello from host!" > /tmp/docker-data/hello.txt
    cat /tmp/docker-data/hello.txt

    # start the container
    sudo docker run -it --name ubuntu-with-data -v /tmp/docker-data:/data ubuntu bash

    # in the container
    cat /data/hello.txt
    echo "Goodbye from ubuntu-with-data!" >> /data/hello.txt
    cat /data/hello.txt
    exit

    # in the host
    cat /tmp/docker-data/hello.txt
    ```

11. docker rm
    ```bash
    sudo docker rm -f hello-world ubuntu ubuntu-top ubuntu-with-data
    ```
