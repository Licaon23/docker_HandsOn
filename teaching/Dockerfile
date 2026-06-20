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

# Give execution permission to script.R
RUN chmod +x /scripts/script.R

# Add /scripts foder to the PATH environment variable
ENV PATH="$PATH:/scripts"
