ARG PYTHON_VERSION=3.11-trixie
FROM python:${PYTHON_VERSION}
SHELL ["/bin/bash", "-l", "-c"]

#####################################
# Set Timezone
#####################################

ARG TZ=UTC
ENV TZ=${TZ}

WORKDIR /var/app
COPY . .

COPY setup.sh /usr/local/bin/
RUN set -eu && chmod +x /usr/local/bin/setup.sh

RUN apt-get update && apt-get install -y curl wget gnupg2 systemd gettext-base
RUN set -eu && \
    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash && \
    export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
    nvm install 24.11.0 && \
    npm install -g pm2
    
# Set environment variables for Poetry
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

RUN /usr/local/bin/python -m pip install --upgrade pip && \
/usr/local/bin/python -m pip install --no-cache-dir poetry

# Expose optional API port for PM2 dashboard
EXPOSE 9615

ENTRYPOINT ["/bin/bash", "-l", "-c", "setup.sh"]
