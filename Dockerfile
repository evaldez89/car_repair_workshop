FROM  gcr.io/iterativo/dockerdoo:13.0
ENV ODOO_EXTRA_ADDONS /mnt/extra-addons
USER root
RUN sudo mkdir -p ${ODOO_EXTRA_ADDONS}
COPY --chown=${ODOO_USER}:${ODOO_USER} . ${ODOO_EXTRA_ADDONS}/car_workshop
RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends build-essential \
    && find ${ODOO_EXTRA_ADDONS} -name 'requirements.txt' -exec pip3 --no-cache-dir install -r {} \; \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*
USER ${ODOO_USER}