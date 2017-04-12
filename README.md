# logdash

A minimalist simple web interface displaying logs history from client machines.

Using psutil, flask, request & mongodb.


```
virtualenv logdashenv
. logdashenv/bin/activate
pip install -r requirements.txt
```

## For the moment

Launch the flask test app from the _flask_test_ folder.

```bash
python consume.py
```

Then launch the periodic script which fetch the system informations from the _fetch_metrics_ folder

```bash
python fetch_metrics_periodically
```

It's aliiive!

## Demo data

The _fetch_metrics/example_output.json_ contains an example of collected data.
