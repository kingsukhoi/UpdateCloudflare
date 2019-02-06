# Update Cloudflare
This program is designed to take list of FQDN to update in CloudFlare and update the entries to your local IP.

# How to run

## Without Docker
 `./driver.py <location of confiTg.json>`
 
## With docker
This is designed to work with Docker Secrets, due to the fact that the majority of the data is sensitive. 

That being said, it will still work with a volume mount.

The command to run this is `docker run -d kingsukhoi/UpdateCloudflare <path in container to config file>`

# Inspiration
I didn't like DDClient, and originally wanted a simple script that could be run through Cron.

The reason there is a docker image, is because I am working at making a fully containerized enviroment.


# TODO
- [] Add example json config 
