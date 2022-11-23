# Documentation

1. [Command line options](./command-line-options.md)
2. [Managing Dependencies](./managing-dependencies.md)

## Event

Event is a thing that happens, esp of importance.
Locust lets you do tasks at certain circumstances using the **Event Hooks**.

Common Examples:
- Preparing test data pre run
- Cleaning test data post run
- Handling failing requests
- Shutdown locust instance after the test passes

### Events Available

- test_start
- test_stop
- on_locust_init
- request_failure
- request_success
- reset_stats
- user_error
- report_to_master
- ...

### Usage

1. Import the class
2. Use the desired decorator + type of event
3. Recommended to add **kwargs argument

### Custom EventHook

Design your own events extending `EventHook` class.
Use `reverse=True` to fire events in the reverse order.

### Distributed Load Testing

Start script with master conf and worker conf in separate windows.

Things to note:
- Locust scripts must be present in all master and worker nodes
- num_users > num_user_classes * num_workers

By default, it uses port 5557, which can be changed, if needed.
