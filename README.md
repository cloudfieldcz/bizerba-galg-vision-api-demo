# Bizerba Galg Vision API Demo

## How to update to a new version

### Automatically

Can't be done. Server is hidden behind VPN.

### Manually on server

Start Fajné OpenVPN. Connect to Fajné Ubuntu server. And run the following commands:

```shell
# Bizerba Galg Vision API Demo directory
cd ~/bizerbagalgvisionapidemo/
# Pull new image
docker compose pull
# Restart container
docker compose up -d
# Remove unused images
docker image prune --force --filter="label=app=galg-vision-api-demo"
```

### Manually on local machine

Prerequisites:

1. Installed [act](https://nektosact.com/installation/index.html)
2. Create file `.local/act/event.json` with the following content:
    ```json
    {
      "act": true
    }
    ```
3. Create file `.local/act/.secrets` with the following content (change `SSH_PASSWORD` value to the correct one):
    ```text
    SSH_HOST=192.168.1.192
    SSH_PORT=22
    SSH_USERNAME=cloudadm
    SSH_PASSWORD=FILL_ME_PLS
    ```

Start Fajné OpenVPN. And run the following commands:

```shell
act
```
