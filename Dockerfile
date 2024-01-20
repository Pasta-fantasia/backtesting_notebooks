FROM jupyter/base-notebook:lab-3.4.8

ENV JUPYTER_ENABLE_LAB=yes
ENV TALIB=0

USER root

# Ensure build-deps
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    fonts-dejavu \
    gfortran \
    build-essential libssl-dev libmariadb3 libmariadb-dev \
    gcc \
    git openssh-client && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# TA LIb system part
WORKDIR "/talib-src"
COPY docker_talib_install.sh /talib-src

RUN if [[ $TALIB == 1 ]] ; then  \
     bash /talib-src/docker_talib_install.sh ; \
    fi

# bokeh insede notebooks
RUN conda install -c conda-forge ipywidgets ; \
    conda install jupyter_bokeh ; \
    jupyter nbextension enable --py widgetsnbextension

USER ${NB_UID}

WORKDIR ${HOME}
COPY requirements.txt ${HOME}

RUN pip install --user -r ${HOME}/requirements.txt

# TA LIb python part
RUN if [[ $TALIB == 1 ]] ; then  \
     pip install --user  TA-Lib ; \
    fi

WORKDIR "${HOME}/work"


