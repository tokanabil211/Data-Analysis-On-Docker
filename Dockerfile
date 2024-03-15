# Use Ubuntu as the base image
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy


RUN mkdir -p /home/doc-bd-a1


COPY train_titanic.csv /home/doc-bd-a1/

CMD ["/bin/bash"]
