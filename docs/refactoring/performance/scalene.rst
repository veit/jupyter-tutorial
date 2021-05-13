scalene
=======

scalene creates profiles for CPU and memory very quickly. The overhead is
usually very low at 10-20%.

.. seealso::
   * `GitHub <https://github.com/emeryberger/Scalene>`_
   * `PyPI <https://pypi.org/project/scalene/>`_
   * `scalene-paper.pdf
     <https://github.com/plasma-umass/scalene/blob/master/docs/scalene-paper.pdf>`_

Installation
------------

Linux and WSL
~~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install scalene

MacOS
~~~~~

.. code-block:: console

    $ brew install --HEAD emeryberger/scalene/libscalene

Use
---

.. code-block:: console

    $ pipenv run scalene test/testme.py

You can display all available options with

.. code-block:: console

    $ pipenv run scalene --help
    scalene --help
     usage: scalene [-h] [--outfile OUTFILE] [--html] [--reduced-profile]
                    [--profile-interval PROFILE_INTERVAL] [--cpu-only]
                    [--profile-all] [--profile-only PROFILE_ONLY]
                    [--use-virtual-time]
                    [--cpu-percent-threshold CPU_PERCENT_THRESHOLD]
                    [--cpu-sampling-rate CPU_SAMPLING_RATE]
                    [--malloc-threshold MALLOC_THRESHOLD]

     Scalene: a high-precision CPU and memory profiler.
                 https://github.com/emeryberger/scalene
                 % scalene yourprogram.py

     optional arguments:
       -h, --help            show this help message and exit
       --outfile OUTFILE     file to hold profiler output (default: stdout)
       --html                output as HTML (default: text)
       --reduced-profile     generate a reduced profile, with non-zero lines only (default: False).
       --profile-interval PROFILE_INTERVAL
                             output profiles every so many seconds.
       --cpu-only            only profile CPU time (default: profile CPU, memory, and copying)
       --profile-all         profile all executed code, not just the target program (default: only the target program)
       --profile-only PROFILE_ONLY
                             profile only code in files that contain the given string (default: no restrictions)
       --use-virtual-time    measure only CPU time, not time spent in I/O or blocking (default: False)
       --cpu-percent-threshold CPU_PERCENT_THRESHOLD
                             only report profiles with at least this percent of CPU time (default: 1%)
       --cpu-sampling-rate CPU_SAMPLING_RATE
                             CPU sampling rate (default: every 0.01s)
       --malloc-threshold MALLOC_THRESHOLD
                             only report profiles with at least this many allocations (default: 100)
