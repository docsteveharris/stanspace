# Stan Workbench

## Build
```
cd dkr
docker-compose build
```
Be patient; this takes a while to complete the build and the load.
To stop, hit `ctrl-c` from the terminal.

The _dkr/workbench_ host folder is mapped to the _work_ folder in the notebook container.

## Running
```sh
docker-compose up -d
```

## Alternatively, combine the build & run steps
```sh
docker-compose up --build -d
```

## Output
To inspect the logs
```sh
docker logs -f stanspace
```

## Using the container's IPython
From the host's command line; useful if you wish to ssh in remotely
```sh
docker-compose exec lab ipython
```
_Note that the stack needs to be up and running for this to work_

## Stopping 
```sh
docker-compose down
```

## Additional notes

### PyStan in Jupyter
The PyStan package isn't compatible with the `asyncio` event loop used internally by Jupyter.  
As a workaround there are two options:  
1. Run the following at the top of any Python notebooks that will call `PyStan`:
```python
import nest_asyncio
nest_asyncio.apply()
del nest_asyncio
```
2. Use the `pystan-jupyter` package which performs the above:  
```python
import stan_jupyter as stan
```


