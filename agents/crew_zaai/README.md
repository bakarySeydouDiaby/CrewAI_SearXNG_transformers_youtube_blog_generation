# AI Agents

**Steps to run the code:**
1. Create a virtual environment with python 3.10.0

```bash
# check versions of python 
## asdf must be installed before
asdf list python    
asdf list python
# choose python 3.10
asdf local python 3.10.0    
python3 -V
# virtual env
python3 -m venv venv_crewai_3.10.0
# activate
source venv_crewai_3.10.0/bin/activate
```

4. Install the required requirements
    - `pip install -r requirements.txt`

5. Create a folder called `assets/` to store the results

6. Add an .env file under `ai-agents/crew_zaai/src/crew_zaai/.env` with:
   ```
    YOUTUBE_API_KEY=<Your key>
    OPENAI_API_KEY=<Your key>
    # for searxng, we ran it as docker container in order to be able to generate an API token which is mandatory for the first agent of our crew
    SEARXNG_BASE_URL=httplocalhost:8080
   ```

7. Run the main.py file

`python3 main.py "Name of the topic for which we create blog"`


8. Result

Open the report.html file on navigator to see the content generated at the end



## Folder Structure:
------------

    ├── crew_zaai
    │
    ├──── src/crew_zaai
    ├────── assets                      <- results
    ├────── config                      <- agent and taks definition files
    ├────── tools                       <- tools to be used by the agents
    │
    │────── .env                        <- file with enviroment variables
    │
    │────── requirements.txt            <- package version for installing
    │
    │────── crew.py                     <- crew definition
    └────── main.py                     <- file to generate the blog post
--------
