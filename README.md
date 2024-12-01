# Cyberpunk 2077: Automatic Protocol Breacher

![Terminal Output](images/terminal_output.png)


## How's it goin, Chooms?

Let's get down to biz, but beware of incoming Cyberpunk slang. As someone who loves Cyberpunk 2077 and Netrunning, this is just a fun project for one of my favorite games. And besides, who doesn't wanna escape from Realspace from time to time? 

It is still in it's early stages, but this script works enough to provide all solutions uploading the most (or at least best) hexcode sequences to any access point breach problem you will find in the game. As of now, it uses heuristics and recursiion to traverse the matrix, applying the game's logic for terminating nonviable paths. 

In the future, it will have two algorithm options: finding all possible solutions and finding the shortest possible solution that uploads the best hexcode sequences with the minimal amount of buffer used. The latter will hopefully apply heuristcs more cleverly. I am still developing a way to handle branching path solutions for the comprehensive solution finder in addition to an image processing and image text recognition pipeline so eventually, the input will just be a picture of the access point. Preem, right?

I also added some unncessary ascii art, neon colors, and messages found on access points in game to make it more fun. 

This is a command line tool built in linux that uses python3, conda, and some fun dependencies (for image processing later). I assume it will work on windows, but I have not tested it so your mileage may vary. 

Enjoy! Now go make some eddies.


## Installation

First things first, slot the shard for the detes. 

Install git and conda. For information on how to do that, start here: [Install Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

This utilizes a conda environment to manage the packages. I found this to be the easist deployment method, but install may take awhile.

Here are the install commands

```
git clone https://github.com/bnjenner/Cyberpunk_2077_Breach_Protocol.git
cd Cyberpunk_2077_Breach_Protocol
conda env create -f environment.yml
conda activate breach_protocol
```

Now, make the script executable. The command below is for linux. I imagine it is not hard to do something similar on windows.

```
chmod +x breach_protocol.py
```

Nova, now time to get cracking, just don't go poking the wrong bears. Don't wanna get zeroed by Netwatch.


## Usage

Inputs
* FRAME: the matrix you are trying to crack
* SEQUENCES: the sequences you are trying to upload
* BUFFER_SIZE: your buffer size

```
./breach_protocol.py sequence.csv frame.csv BUFFER_SIZE
```
