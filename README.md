# polymath

`polymath` is a utility that can answer free-form questions based on a corpus of federated content.

Each `polymath` instance defines a set of endpoints of federated content it
wants to be able to use, each with a short name e.g. 'Dimitri' or 'Alex'.

The federated endpoints contain pre-computed embeddings of chunks of content.

When `polymath` receives a question, it first computes an embedding for the
query. Then it hits each federated endpoint to select chunks of content most
relevant to the question. Then it injects as many chunks of content into a
prompt as will fit, appends the question, and uses the OpenAI completions API to
answer the question.

## Sample

`sample/` includes a sample question answerer.

To run it, ensure you have an environment variable set for `OPENAI_API_KEY`.

Alternatively, create a `.env` file with these contents:

```
OPENAI_API_KEY=<key goes here>
TRANSFORMERS_VERBOSITY=error
```

(The last line will suppress the `None of PyTorch, TensorFlow >= 2.0, or Flax have been found` warning you may get when running the code)

Any embeddings pkl files you have in `out/` will be used as the content. If none exist, it will use the `sample-import-content.pkl`.

Then run `python3 -m sample.main "How does building a platform differ from building a product?"`

## Creating a new pkl

To create a new pkl file for a source, first, create a json object like this:

```
{
  chunks: [
    text: '<raw text>',
    //all of the following are optional
    url: '<URL>',
    image_url: '<IMAGE_URL>',
    title: '<TITLE>',
    description: '<DESCRIPTION>',
  ]
}
```

Then run `python3 -m converter <FILENAME>`. It will create a new file with the same name but a `.pkl` extension in the `out/` directory.

### Running the server

To start the host server, run `python3 -m host.server`. It will start a Flask app as a local server. Go to `http://127.0.0.1:8080/api/query` to see the API endpoint.

### Developing

It's recommended to use `virtualenv` to manage your python environment for this project.

If you don't have `virtualenv`, install it with `pip install virtualenv`.

After checking out the repo, create a virtualenv:

`virtualenv env`

Every time you open a new terminal, activate the environment with `source env/bin/activate`.

After checking out the repo and activating your environment install dependencies: `pip install -r requirements.txt`

Every time you add a new depenency, update the dependency list with `pip freeze > requirements.txt`
