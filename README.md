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
```
docker-compose up -d
```

And then to inspect 
```
docker logs -f stanspace
```

## Using the container's IPython
From the host's command line; useful if you wish to ssh in remotely
```
docker-compose exec lab ipython
```

## Stopping 
```
docker-compose down
```


