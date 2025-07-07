# Genovation Assignment
##  Backend Development Internship Test Submission

## Installation

1.Clone the repo

```bash
  git clone https://github.com/Dipanshu-04/Genovation_Assignment.git
  ```
```bash
cd Genovation_Assignment
```
Install prerequisite python packages:

```bash
  pip install requirements.txt
```

    
## Run Locally

Start the server

```bash
  uvicorn main:app --reload
```
The main API will be available at : 

http://127.0.0.1:8000/

Access Docs at :

http://127.0.0.1:8000/docs

### Curl Commands
**1. Login** 

```bash
curl -X POST http://127.0.0.1:8000/login \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"<username>\", \"password\": \"<password>\"}"

```

**Response**

```bash
{
  "access_token": "<your_access_token>"
  }

```

**2.Submit a Prompt**

```bash
curl -X POST http://127.0.0.1:8000/prompt \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_access_token>" \
  -d "{\"prompt\": \"Tell me a joke\"}"
```

**Response**

```bash
{
  "response": "Why did the Python programmer wear glasses? Because he couldn't C!"
  }
```

**3. Get prompt History**

```bash
curl -X GET http://127.0.0.1:8000/history \
  -H "Authorization: Bearer <your_access_token>"
```
**Response**

```bash
{
  "user1": [
    {
      "timestamp": "2025-07-07T18:00:44",
      "prompt": "Hello, FastAPI!",
      "response": "I'll need a second to consider it."
    }
    {
      "timestamp": "2025-07-07T18:01:03",
      "prompt": "Tell me a joke",
      "response": "Why did the Python programmer wear glasses? Because he couldn't C!"
    }
  ]
}
```


### Hardcoded User Credentials

| Username | Password  |
| -------- | --------- |
| user1    | abcd      |
| user2    | 1234      |


**Note:** This app does not include user registration — users are predefined.


## Known Limitations

- User credentials are hardcoded (no registration).
- dummy responses are used for prompt.
- Prompt history is stored in a local history.json file (not persistent across machines).
- No frontend UI — API only.
- JWT tokens are  minimally signed; not production-grade auth.


