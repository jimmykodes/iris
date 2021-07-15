# Use Machine Learning to Cluster HTML Attributes

A dumb little poc that you can use ML to cluster HTML attributes.
No idea why you'd want to though...

This will load in the iris dataset, train-test split the data,
load the training and testing data in to html attributes to be
read and trained on. Testing data can be posted to the `/test`
endpoint to get the number correct and the accuracy score.

## Running

### Install python requirements

```shell
pip install -r requirements.txt
```

### Run the Flask server
```shell
cd src
flask run
```
The server can now be accessed at `http://localhost:5000`

### Run the ML

In a new terminal tab
```shell
./clusterer/app.py
```

This will print out the number correct out of the 50 testing points
as well as the accuracy score.
