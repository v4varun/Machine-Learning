###################################################
Install and set up Open AI
###################################################

# Go to this URL
https://platform.openai.com/docs/quickstart

# Show that it has steps for 

cURL
python
NodeJS

# Let's show that you can hit the API using cURL

# Show where you can download cURL
# No need to click through anything, just show this page

https://everything.curl.dev/get

# On the terminal

curl --version

# Set up the API key

# Go the the Open AI page

# Click on API keys on the left sidebar

Name: learning-openai-apis

# Create and copy the key over

----------------------------------------------
# Make API requests using cURL
----------------------------------------------


# Now let's make a curl request to the API
# Replace $OPENAI_API_KEY with the actual API token when you make the request


# Let's retrieve all the models available (replace the key in the header)

curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"

# Show large number of models returned

# Let's retrieve the details of some specific models

# https://platform.openai.com/docs/models/continuous-model-upgrades

curl https://api.openai.com/v1/models/gpt-4-0613 \
  -H "Authorization: Bearer $OPENAI_API_KEY"


curl https://api.openai.com/v1/models/dall-e-3 \
  -H "Authorization: Bearer $OPENAI_API_KEY"


# Now let's send a prompt using the API

# https://platform.openai.com/docs/api-reference/chat/object

curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json"   \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "Could you recommend some resources I could use to learn Python programming?"
      }
    ]
  }'

curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json"   \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a teaching assistant for a Math course"
      },
      {
        "role": "user",
        "content": "How do I solve 3x + 5 = 32? Could you give me step by step instructions?"
      }
    ]
  }'


# Use a different model

curl https://api.openai.com/v1/chat/completions \
-H "Content-Type: application/json"   \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": "You are a sarcastic teenager who is bored with everything in life talking to an adult"
      },
      {
        "role": "user",
        "content": "How are things with you? Have you figured out what colleges you want to apply to?"
      }
    ]
  }'


curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Who won the cricket world cup in 2011?"
      },
      {
        "role": "assistant",
        "content": "India won the cricket world cup in 2011."
      },
      {
        "role": "user",
        "content": "Where was it played? Do you know the details of the final match?"
      }
    ]
  }'


----------------------------------------------
# Set up virtual environment
----------------------------------------------

# - Please do this in a terminal window on your local machine

# Start in a folder ~/projects

python --version

jupyter --version

mkdir open_ai_apis

cd open_ai_apis

python3 -m venv openai_venv

ls -l

source openai_venv/bin/activate

# Note the command prompt change

# Environment activation for Windows (FYI nothing for the recording)

# openai_venv\Scripts\activate.bat


# IPython kernel (ipykernel) is a Python package that provides the communication between the Jupyter Notebook or JupyterLab interface and the Python kernel. It enables you to run Python code interactively and display the output within the notebook environment.

pip install ipykernel

# This will list the kernels available (only one Python3 kernel - remove all others)

jupyter kernelspec list

# Install and make the pytorch_venv kernel available to Jupyter Notebooks

python -m ipykernel install --user --name=openai_venv

# Now we have 2 kernels available

jupyter kernelspec list

 # Upgrade pip

pip install --upgrade pip

# Required libraries in virtual environment

pip install openai

openai --version

pip install pandas matplotlib

# Start jupyter notebook

jupyter notebook

# Create a new notebook 

# IMPORTANT: Make sure the notebooks is using the openai_venv virtual environment
# Go to Kernel -> Change kernel to set the virtual environment
# Will need to do this for each notebook












