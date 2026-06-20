# Docker instructions

## Task 1: Create Dockerfile as a text with instructions

```dockerfile
# Start from debian linux image (DockerHub)
FROM debian:stable

# Add custom label
LABEL maintainer="arodrigo <albert.rodrigo23@gmail.com>" \
      version="0.1" \
      description="This is a hand-on exercise to practice Docker"

# Install R (after apt-get update)
RUN apt-get update && apt-get install -y r-base

# Install R package 'optparse'
RUN R -e 'install.packages("optparse", repos = "http://cloud.r-project.org/")'

# Make the folder '/scripts' in the container
RUN mkdir /scripts

# Copy 'scripts/script.R' to the folder '/scripts' in the container
ADD scripts/script.R /scripts
```

`RUN` -> command to RUN commands, like installing, creating directories, etc.

`ADD` -> command to copy folders or files inside the container.

```dockerfile
ADD scripts/script.R /scripts
```

`ENV` -> to modify environament variables.


## Task 2: Create image from the Dockerfile

```bash
sudo docker build -t teachingimage .
```

Build an image from DockerFile, in the current directory, whose name Will be teachingimage.

To check which images are available:

```bash
sudo docker images
```


## Task 3: from a given image, create a container

```bash
sudo docker run imageName
```


## Task 4: run it interactively

But to run it interactively add the `-i -t` flags:

```bash
sudo docker run -it teachingimage
```

Show the containers that have been run:

```bash
sudo docker ps -a
```

To remove a given container:

```bash
sudo docker rm <containerID>
```

Or all:

```bash
sudo docker rm $(sudo docker ps -a -q)
```


## Task 5 and 6

In this exercise we want to run an R script to perform some work. To do so from anywhere we need to grant execution permissions and add the foler where the `script.R` is to the PATH environment were exectuables are searched.

This need to be written in the image otherwise, if we do it interactively in the containers, changes Will not be saved once we exit the container.

Now, we can run the `script.R --help` not interactively as:

```bash
sudo docker run my_image2 script.R --help
```


## Task 7: use the script.R to produce output

In the same directory where I run the script, I create using interactive R a file with random numbers. Then I call the funciton:

```bash
script.R -i input.txt -o histrogram.pdf > summary.txt
```

The function prints a summary, which I redirect to a file `summary.txt`.


## Task 8: use volumes to store results within the container

### Here I had to create a dataset inside the container. But when I exit, it disappears...

To run the script in the containers with a dataset outside it, we use volumes and bind mounts.

First, we create a volumen, manage by docker: a folder

```bash
sudo docker volumen create data
```

THen, connect the volumen to the container:

```bash
sudo docker run -it -v data:/scripts/data my_image2
```

- `data` is the name of the volumen
- `/scripts/data` is the directory where the host folder Will appear

Now, we créate the input data inseide the volum, run the script and store the results in the data directory. So it still exists once we exit and enter again.

```r
R
> write.table(rnorm(1000,mean=0,sd=1),file="scripts/data/input.txt",row.names=FALSE,col.names=F)
quit()
```

```bash
script.R -i scripts/data/input.txt -o scripts/data/hist.pdf > scripts/data/summary.txt
```

TO check which columes are available:

```bash
sudo docker volumen ls
```

To inspect the content of a given volum:

```bash
sudo docker volume inspect data
```

```json
[
    {
        "CreatedAt": "2026-03-28T19:07:10+01:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/data/_data",
        "Name": "data",
        "Options": null,
        "Scope": "local"
    }
]
```

Then check the directory Mountpoint:

```bash
sudo ls -l /var/lib/docker/volumes/data/_data
```

```text
total 32
-rw-r--r-- 1 root root  4580 Mar 28 19:12 hist.pdf
-rw-r--r-- 1 root root 18201 Mar 28 19:12 input.txt
-rw-r--r-- 1 root root   144 Mar 28 19:12 summary.txt
```

If I run the container without mounting the volumen, these data won't be there; otherwise, when mounted the volum, they Will be available.


## Task 9: use bind mounts to use input data locally to run script.R within the container and store results locally

### This serve to store the files generated within the container into a volumen stored in the host

Howver, how to use data from the host as intput for our software within the container?

Use bind mounts.

Here, let's use a bind mount to use `data/normal.txt` as input for script:

```bash
docker run -v <path/to/bind_mount/host>:<path/to/bind_mount/container> -w <working_dir> <image>
```

```bash
sudo docker run -v $PWD/data:/scripts/data my_image2 script.R -i /scripts/data/normal.txt -o scripts/data/hist.pdf > results/summary.txt
```
