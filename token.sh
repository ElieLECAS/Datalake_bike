az storage blob generate-sas \
    --account-name elecas.ext@simplonformations.onmicrosoft.com \
    --container-name data \
    --name product_eval \
    --permissions r \
    --expiry <2024-11-DDTHH:MM:SSZ> \
    --auth-mode key
