# Cyberpunk 2077: Automatic Protocol Breacher

## What's up, Chooms?

As someone who loves Cyberpunk 2077 and Netrunning, this is just a fun project for one of my favorite games. 

It is still in it's early stages, but this script works enough to provide the best solution to any access point breach problem you will find in the game. As of now, it uses a recursive pseudo brute force method that automatically terminates nonviable paths through the matrix. 

Ideally, it will eventually return all possible solutions, but I am still developing a way to handle branching path solutions. I also am working on image processing and image text recognition so eventually, the input will just be a picture of the access point. 

I also added some unncessary ascii art, neon colors, and messages found on access points in game to make it more fun. 

This is a command line tool built in linux that uses python3, conda, and some fun dependencies (for image processing later). I assume it will work on windows, but I have not tested it so your mileage may vary. 

There is no GUI. A real Netrunner would use the terminal, anyway, so I am gonna gate keep a bit.

I hope you enjoy!


## Installation

First things first, install git and conda on your sysem. For information on how to do that, start here: [Install Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

This utilizes a conda environment to manage the packages. I found this to be the easist deployment method, but install may take awhile.

Here are the install commands

```
git clone https://github.com/bnjenner/Cyberpunk_2077_Breach_Protocol.git
cd Cyberpunk_2077_Breach_Protocol.git
conda env create -f environment.yml
conda activate breach_protocol
```

Now, make the script executable. The command below is for linux. I imagine it is not hard to do something similar on windows.

```
chmod +x breach_protocol.py
```

Preem, now go make some eddies!


## Usage

