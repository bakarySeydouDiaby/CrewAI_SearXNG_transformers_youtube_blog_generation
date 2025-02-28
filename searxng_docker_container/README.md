what is searxng
===============
    SearXNG is a privacy-respecting metasearch engine
    SearXNG doesn't natively support API keys out of the box. 

    if you set 'authentication: True' in the settings.yml, 
    then SearXNG will require an API key for searches. 
    The API key is generated using a secret key 
    that's also defined in the settings. 
    So the user needs to generate a secret key, 
    set it in the configuration, and then users 
    can get their API key by using the '/preferences' 
    endpoint, which gives them a unique key based 
    on their user token and the server's secret.

    So the steps would be:
    ----------------------

    1. Deploy SearXNG via Docker, setting up the docker-compose.yml with the correct volumes for configuration.

    2. Create a settings.yml file where authentication is enabled, a secret key is set, and perhaps other configurations.

    3. The secret key is used to sign the user tokens, generating the API keys.

    4. Users can then access the /preferences page to retrieve their API key, which they include in their requests.

    the user can manually generate an API key by creating a user_token and then computing the HMAC with the server's secret.
    
    So to make this work, the user needs to:
    ---------------------------------------

    1. Set authentication to true in settings.yml.

    2. Define a server.secret_key.

    3. Generate an API key by picking a user_token (like a username or arbitrary string) and computing the HMAC-SHA256 of it with the secret_key.

    4. Use that API key in requests by appending '&key=...' to the search URL.

the step-by-step plan is:
=========================

1. Create a directory for the SearXNG setup.

2. Create a docker-compose.yml with the SearXNG image and volume mounts for settings.

3. Generate a secret key (e.g., using openssl rand -hex 32).
    `openssl rand -hex 32 > secret_key`

4. Create settings.yml with authentication enabled and the secret key.

5. Start the container with docker-compose up.
    `docker-compose up -d`
6. Access the /preferences page to get the API key, or generate it manually.

7. Generate an API Key  mannually
Manual Token Generation

Step 1: Get the Secret Key
    `SECRET_KEY=$(cat secret_key)`
     

Step 2: Create a User Token
Generate a random user token (replace your_username):

```bash
USER_TOKEN="bakary-$(openssl rand -hex 16)"
echo "User Token: $USER_TOKEN"
```

Step 3: Compute the API Key

```bash
API_KEY=$(echo -n "$USER_TOKEN" | openssl dgst -sha256 -hmac "$SECRET_KEY" | awk '{print $2}')

echo "API Key: $API_KEY"
```

Test the key:
============
`curl "http://localhost:8080/search?q=test&format=json&key=$API_KEY"`






8. Use the API Key in Requests
Include the API key in your search requests:

curl "http://localhost:8080/search?q=test&format=json&key=${API_KEY}"

Notes:
======
Persistence: The secret_key and settings.yml are stored in your host directory, ensuring keys survive container restarts.

Rate Limits: Adjust authentication.token.limit in settings.yml to control request rates.

Security: Expose SearXNG via HTTPS (e.g., using Nginx/Caddy as a reverse proxy).

Verification
============
    Check if the API key works:
    curl -v "http://localhost:8080/search?q=test&format=json&key=INVALID_KEY"  
        # Should return 403
    curl -v "http://localhost:8080/search?q=test&format=json&key=${API_KEY}"  
        # Should return 200



autre doc :
=========


docker pull searxng/searxng
Installer le container (je le force sur le port 8888, pour être tranquille, vous pouvez choisir un autre port)

docker run --restart=always -d -p 8888:8080 \
           -v "${HOME}/searxng:/etc/searxng" \
           -e "BASE_URL=http://localhost:8888/" \
           -e "INSTANCE_NAME=doLys_search" \
           --name mois_annee__searxng \
           searxng/searxng

pour utiliser, taper ==> localhost:8888