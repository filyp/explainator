# explainator
## Setup
### Win
1. Download and install cmder tool - [cmder][cmder].
2. Download and install Python 3.7.4 from [here][python]. During installation, remember to check "Add Python 3.7 to PATH" and  "Disable PATH length limit" options (the second one is optional).
3. Launch cmder
	- Go to directory where you want to store repo
	- Execute:
        ```sh
        git clone https://github.com/fsondej/explainator.git`
		cd explainator
		```
	- Then, execute following lines:
    	```sh
        bash
    	chmod +x windows.sh
    	./windows.sh
        ```

### Linux, MacOS
1. Make sure you've got installed any python3 distribution. You might need to use your package manager (e.g. brew, apt-get) to get it done.
2. Launch command line tool of your selection
	- Go to directory where you want to store repo
	- Execute:
        ```sh
        git clone https://github.com/fsondej/explainator.git`
		cd explainator
		```
	- Then, execute following:
    	```sh
    	chmod +x nix.sh
    	./nix.sh
    	```
## How to run examples in notebook
After installation, use the command line tool of your choice to change working dir to local repository instance. Then, execute:
```sh
jupyter notebook
```
Afterwards, you should be able to open and run notebooks placed in repo. Make sure you've selected **explainator-py** kernel in jupyter gui in your browser - selected kernel should be visible somewhere in the top right corner.



[cmder]: <https://cmder.net/>
[python]: <https://www.python.org/downloads/windows/>
