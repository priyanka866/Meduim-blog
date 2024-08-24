FROM python:3.9

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         nginx \
         python3-pip \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org gevent gunicorn && \
        rm -rf /root/.cache

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY . /opt/program
WORKDIR /opt/program

#make serve executable
RUN chmod +x /opt/program/serve

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt