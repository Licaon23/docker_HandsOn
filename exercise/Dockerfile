# Start from debian linux image (DockerHub)
FROM debian:stable

# Add custom label
LABEL maintainer="arodrigo <albert.rodrigo23@gmail.com>" \
      version="0.1" \
      description="This is a hand-on exercise to practice Docker"

# Install python 3 (after apt-get update)
RUN apt-get update && apt-get install -y python3

# Make the folder '/scripts' in the container
RUN mkdir /scripts

# Copy 'scripts/script.R' to the folder '/scripts' in the container
ADD seqClass.py /scripts

# Give execution permission to script
RUN chmod +x /scripts/seqClass.py

# Add /scripts foder to the PATH environment variable
ENV PATH="$PATH:/scripts"
