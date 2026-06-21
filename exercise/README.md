# Sequence classifier script

This Python script classifies an input nucleotide sequence as DNA, RNA, both possible, or neither. It can also optionally search for a motif inside the sequence.

## Purpose

The script is designed to:

- read a sequence from the command line
- check whether it contains only valid nucleotide characters
- determine whether it is DNA or RNA
- optionally search for a motif within the sequence

## Installation

The `seqClass` script can be directly downloaded from this repository:

```bash
wget https://github.com/Licaon23/docker_HandsOn/tree/master/exercise/seqClass.py
```
Also, a public `seqClass` Docker image is available in the Docker Hub and can be downloaded as follows:

```bash
docker pull arodrigo23/seqclass:0.1
```

## Use docker image

To execute seqClass with docker:

```bash
docker run arodrigo23/seqclass:0.1 seqClass.py -s ACGT
```

### With motif search

```bash
docker run arodrigo23/seqclass:0.1 seqClass.py -s ACGTACGT -m GTA
```
