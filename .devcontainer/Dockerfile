# [Choice] Pypy version: 2, 3
ARG VARIANT="3"
FROM pypy:${VARIANT}

# Use the [Option] comment to specify true/false arguments that should appear in VS Code UX
#
# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
COPY library-scripts/*.sh library-scripts/*.env /tmp/library-scripts/
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true"\
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends libblas-dev liblapack-dev gfortran libopenblas-dev libgeos-dev npm

# ライブラリ・補助ツールインストール
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt \
    && pip install git+https://github.com/not522/ac-library-python \
    && pip install online-judge-tools pipenv
RUN npm install -g atcoder-cli

# atcoder-cli設定
ARG HOME_DIR=/home/$USERNAME
USER $USERNAME
WORKDIR $HOME_DIR/.config/atcoder-cli-nodejs/python
COPY template.json ./
RUN touch ./main.py
RUN acc config default-template python && \
    acc config default-task-choice all
