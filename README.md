# Vacation

This handy little app keeps track of your accumulated and remaining vacation
days.


## Installation

*Vacation* is a Python script, so is installable via **pip**:

* Install: `pip install vacation`
* Upgrade: `pip install -U vacation`
* Uninstall: `pip uninstall vacation`


## Setup

Now that Vacation is installed, let's set up your `.vacationrc` file.
The first two lines in your file must define a starting days value,
and a rate of accumulation.

Run the following:

1. `vacation set days 10`
2. `vacation set rate 15`

Now you can this gives you 10 days (as of today) and a rate of 3 weeks (15 days)
per year of vacation accrual.


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
  e.g. `vacation set days 10.5`
* `vacation Nov 8`: Take a vacation day on November 8
* `vacation Nov 8, 12`: Take two vacation days, on November 8 *and* 12


## Development

Development should be easy!

1. Clone the git repo
2. Create a new virtual env
  * Get Python 3.4 or above, e.g. `brew install python3`
  * `python3.4 -m venv venv`
3. Activate your new virtualenv
  * `source venv/bin/activate`
4. Install requirements from file
  * `pip instal -r requirements`
5. Run tests
  * `nosetests` or `make test`
6. Run the program, using the `run.py` script
  * `python run.py [args]`
7. Make changes. Submit pull requests. Be happy.

You can even install *Vacation* into your virtualenv if you want (`pip install vacation`),
and it will give you the `vacation` without polluting your global installation.
