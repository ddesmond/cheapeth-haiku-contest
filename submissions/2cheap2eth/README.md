#CheapETH Haiku Contest - Submission (2cheap2eth)

## About
Thought it would be cool to generate a haiku off some real time cETH stats

Currently the script generates a supper shitty, 4 line haiku, based off the latest block number and it's time stamp
( The block data is taken from: https://node.cheapeth.org/rpc )


## Pre-requisites
* python >= 3.6
* json-rpc >= 1.13.0
* requests >= 2.23.1

For a full list of requirements, see the requirements.txt file


## Install & Run

0. (optional) Install python virtual environment
1. Navigate to root submission directory (where 2cheap2eth_entry.py is stored)
2. Install the requirements needed to run the script
    * pip install requirements.txt
3. Then run the script
    * python .\2cheap2eth_entry.py

## Example output:

The month was February
And the night was tight
When block number 11878123
Was lost in flight



## Todo:

* add more variation in the haiku's generated