FROM jupyter/datascience-notebook:latest

WORKDIR /home/jovyan/work

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN git clone https://github.com/ITMO-NSS-team/EPDE.git
RUN git clone https://github.com/ITMO-NSS-team/torch_DE_solver.git

COPY replace.py replace.py

RUN python3 replace.py

RUN pip install EPDE/.
RUN pip install torch_DE_solver/.