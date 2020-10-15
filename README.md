# notificaiton-clockify-to-discord
This script translates clockify webhooks into discord notifications

docker build -t clockify-to-discord .

docker run -p 5000:5000 --env WEBHOOK=https://discordapp.com/api/webhooks/... clockify-to-discord 

