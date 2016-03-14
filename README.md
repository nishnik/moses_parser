# moses_parser
Parses the bash script so that you can change it from python program

Output:
```
We can change the following options:

MMMdir
mtdir
mosesdirmine
mosesdir

We have the following parameters set:

MMMdir -> "$mtdir/Moses-for-Mere-Mortals"

mtdir -> "$HOME/Desktop/Machine-Translation"

mosesdirmine -> "$mosesdir"

mosesdir -> "$mtdir/MMM"


Now we change `mtdir` to `$HOME/Desktop`


Now `mtdir` has value: 
"$HOME/Desktop"


And we have the following parameters set:

MMMdir -> "$mtdir/Moses-for-Mere-Mortals"

mtdir -> "$HOME/Desktop"

mosesdirmine -> "$mosesdir"

mosesdir -> "$mtdir/MMM"

Now we write it to a file named `mt-location-1.00(new)`
```
