# Binary Friendship Terminal (>_<)

A tiny binary encoder + decoder terminal I made in Python.

This isn't supposed to be some serious cryptography project or a perfect implementation.

It's a little project I want to keep because it reminds me of **why I started learning Python in the first place: curiosity.**


## What is this?

`binary.py` is a terminal program with:
- a small login window
- a menu-driven terminal
- text to binary encoding
- binary to text decoding
- binary output arranged into groups of 5 blocks per line
- a few unnecessarily goofy messages :3

The terminal literally calls itself:

BINARY FRIENDSHIP TERMINAL (>_<)

because, well...

**Friendship Day.**

:3


## Why did I make this?

### 1 August 2026 : Day 11 of learning Python

I was only about **11 days into learning Python** when I decided to make this.

I was still going through CS50P and had been learning the basics by making tiny programs. I suddenly thought:

> "planned to made binary.py a binary encrypter and decrypter including a login window... rather a sentence lol specified to a username and password"

And because the next day was Friendship Day, I decided to actually make the thing.

At that point I didn't really know what I was doing.

I just knew I wanted the computer to do something interesting.

So I started figuring it out.


## The part where I broke my brain a little

One of the things I needed was a way to turn characters into numbers and then into binary.

That's when I learned about:

`ord()`

and

`chr()`

`ord()` let me convert a character into its numeric character code, while chr() let me turn the number back into a character.

I then started wondering:

> Is every character represented in 7 bits?

That sent me down a tiny rabbit hole about ASCII and character representation.

I remember writing:

> "I have to make computer work not me~"

And honestly, that became the whole point of this project.

I didn't want to manually figure out the binary.

I wanted to make the computer figure it out.


## How the encoder works

For every character entered by the user, the program:

1. gets its character code using `ord()`
2. repeatedly divides the number by 2
3. records the remainders
4. reverses the resulting bits
5. prints the binary representation

The encoder also puts a leading 0 before the seven calculated bits, giving each character an 8-bit-looking block.

For example, the output is arranged roughly like:

0xxxxxxx 0xxxxxxx 0xxxxxxx 0xxxxxxx 0xxxxxxx

0xxxxxxx 0xxxxxxx 0xxxxxxx . . . 

The program prints five binary blocks per line, which was one of the little things I wanted the terminal to do.


## How the decoder works

The decoder takes binary blocks separated by spaces.

For every block, it does:

int(block, 2)

to convert the binary number back into an integer, and then:

chr(...)

to turn that integer back into a character.

So the basic journey is:

TEXT

 | 
 
ord() 

 |

NUMBER

 |
 
BINARY

 |
 
BINARY BLOCKS

 |
 
int(block, 2)

 |
 
NUMBER

 |
 
chr()

 |
 
TEXT


## The login window

Yes.

I also somehow decided this tiny binary converter needed a login system.

The username is:

Adyasha

and the password is:

02082026

The login isn't meant to be secure authentication. It's just part of the goofy little project and the original idea behind it.

After logging in, the terminal says:

Happy Friendship Day <3

because that was the whole reason I was making this thing in the first place.


## The code is messy.

Very messy.

But it works.

And honestly, that's one of the reasons I want to keep this project.

I had only been learning Python for around 11 days.

I didn't know the "proper" way to design everything yet. I was figuring things out while writing them, changing things, asking myself questions, breaking things, fixing them, and then getting excited whenever something finally worked.

Looking at the code now, I can already see things I would probably design differently.

But that's okay.

**This is a snapshot of me learning.**

I don't want to erase that by pretending I knew everything from the beginning (cuz i never did).


## A tiny milestone for me

On the evening of **1 August 2026**, after messing around with the encoder, ASCII, `ord()`, `chr()`, and the rest of the program, I finally wrote:

> "okay...encoder is done !! m soo happyyy ahhhh"

Later that night:

> "sooo yess m done at the end of day and I managed to send it to him <3<3"

And then:

> "and yess I feel good...I feel like I learned things"

That's probably the most important part of this repository.

Not the encoder.

Not the decoder.

Not even the code.

It's the fact that **I had an idea, followed my curiosity, struggled through it, and made the computer do the thing I imagined.**


## What I learned while making this

This project was where I got to practice:

- `ord()`
- `chr()`
- strings
- loops
- `while`
- `for`
- lists
-indexing
- functions
- `main()`
- `sys.exit()`
- `match...case`
- user input
- binary representation
- ASCII
- converting numbers between bases
- basic program flow
- designing a menu-driven terminal program

And probably the most important lesson:

> There are many ways to solve a single problem.

I was still very early in Python when I made this, so this isn't necessarily the best way to implement a binary encoder/decoder.

It's just **my way at that point in time.**


## Running it

Make sure Python is installed, then run:

`python binary.py`

You'll get the terminal:

`BINARY FRIENDSHIP TERMINAL (>_<)`

`Built with Python.
One evening.
One Laptop.
And way too many goofy ideas meoww:3`

Then log in and choose:

`1. Encode
2. Decode
3. Exit`


## A little time capsule

I want to keep this repository for a very simple reason.

This was one of the first times I realized that I could have a random idea in my head and actually make a computer do it.

It was messy.

I broke my brain a little.

I didn't know enough Python.

I definitely didn't write perfect code.

But it worked.

And that's kinda beautiful.

**11 days into Python, I made this.**

I want future me to be able to come back here and remember that version of me.

The one who kept asking questions.

The one who got curious.

The one who went:

> "I have to make computer work not me~"

and then actually did.


## Made by Adyasha

### 1 August 2026

Python || CS50P || curiosity || friendship || way too many goofy ideas :3

`Oink Oink :)`
