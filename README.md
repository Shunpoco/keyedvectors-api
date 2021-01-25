### keyedvectors-API
Thid repository build an API server which we can search `similar words` by `gensim.keyedvectors`.

#### Prerequest
- You should use `pipenv` to manage packages in this repository.

#### Prepare
```shell
pipenv install
pipenv run python set.py
```

#### Run the server
```shell
pipenv run uvicorn main:app --reload
```
Access `http://localhost:8000/similar/glove/twitter?n=5` !

#### Future works
- Train model with wikipedia corpas.
