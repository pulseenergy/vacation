
<pre>
 __   __                           _        _                    
 \ \ / /  __ _     __     __ _    | |_     (_)     ___    _ _    
  \ V /  / _` |   / _|   / _` |   |  _|    | |    / _ \  | ' \   
  _\_/_  \__,_|   \__|_  \__,_|   _\__|   _|_|_   \___/  |_||_|  
_| """"|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
</pre>

This handy little app keeps track of your accumulated and remaining vacation
days.


## Installation

*Vacation* is a Python script, so is installable via [pip](https://docs.python.org/3/installing/):

* Install: `pip install vacation`
* Upgrade: `pip install -U vacation`
* Uninstall: `pip uninstall vacation`

You can even install *Vacation* into your virtualenv if you want (`pip install vacation`),
and it will give you the `vacation` command without polluting your global `site-packages` *or* `/usr/local/bin/`.

## Setup

Now that Vacation is installed, let's set up your `.vacationrc` file.
The first two lines in your file **must** define a starting days value,
and a rate of accumulation.

Run the following:

1. `vacation set days 10`
2. `vacation set rate 15`

This gives you 10 days (as of today) and a rate of 3 weeks (15 days)
per year of vacation accrual. Now you're good to go.


## Usage

The installation will put the `vacation` command in your `/usr/local/bin/`
so you should be able to run it from anywhere.

* `vacation` or `vacation show`: Display vacation days remaining
* `vacation set days N`: Specify, as of today, how many days you have remaining
  * Use this to set up your .vacationrc or to fix your days to a known value,
  e.g. `vacation set days 10.5`
* `vacation set rate N`: Specify, as of today, what rate you accumulate vacation days
  * The rate is in *workdays per year*, e.g. 15 (days per year) = 3 weeks per year.
  * You can adjust your rate any time, if it happens to change
  e.g. `vacation set rate 20`
* `vacation Nov 8`: Take a vacation day on November 8
* `vacation Nov 8, 12`: Take two vacation days, on November 8 *and* 12


## Development

Development should be easy!

1. Get Python 3.4 or above. Not necessary, but comes with venv, so do it.
  * e.g. `brew install python3` on OSX
2. Clone the git repo
  * `git clone git@github.com:pulseenergy/vacation.git`
3. Create a new virtual env
  * `python3.5 -m venv venv`
4. Activate your new virtualenv
  * `source venv/bin/activate`
5. Install requirements from file
  * `pip install -r requirements`
7. Run tests
  * `nosetests` or `make test`
8. Run the program, using the `run.py` script
  * `python run.py [args]`
9. Make changes. Submit pull requests. Be happy.

