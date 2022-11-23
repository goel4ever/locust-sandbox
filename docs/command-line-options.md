# Locust Command Line Options

```shell
Lists out all available command a.k.a help
$ locust -h

List out all the user classes in the locust file
$ locust -f locustfile.py -l

Prints the task execution ratio
$ locust -f locustfile.py --show-task-ratio

```

## Debugging or Smoke Testing

```shell
$ locust -f locustfile.py -u 1 -r 1 -t 10s --headless --print-stats \
    --csv execution.csv --csv-full-history --host=https://example.com

-u    defines number of users to spin up
-r    defines the spawn rate
-t    defines the duration
--headless      skips the UI and runs the script in the terminal
--print-stats   prints all the statistics in the terminal
--csv           stores all statistics in the csv file defined
--csv-full-history Stores full history in the csv file. Has to be used with --csv

You'll see 4 CSVs generated
- *_exceptions.csv
- *_failures.csv
- *_stats.csv
- *_stats_history.csv

Alternatively you can use:
--only-summary
```

## Logging

```shell
$ locust -f locustfile.py -L CRITICAL --logfile mylog.log --html report.html

Logs the information as critical, to the log file
Choices are between DEBUG, INFO, WARNING, ERROR, CRITICAL
The default value is INFO

-L defines the log level to log
--loglevel same as -L
--logfile defines the file name for the logs to be stored in
--html will generate the html report
--skip-log-setup to skip logging setup if not needed. No logs will be generated
```
