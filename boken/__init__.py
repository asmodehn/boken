# TODO : Think about a "nodelet" design, based on async task that schedule themselves.
# This can be in a class : init is hte "reset" behavior, and call is hte "run in a loop" behavior
# We should attempt to make it so that each method is a pure function of hte instance (getting a property) or some more complex functional/categorical concept...
# This design is potentially scalable and distributable to multiple processes (stream processing style)

# Note : there are two interchangeable patterns : queues in/out, or dequeue as buffer, both processing in background. Trading time & space.
# One can be implemented on top of the other...
# Given python problem with the GIL, the buffer implementation over a basic async queue in/out design might be the better approach (despite it being more 'functional style')
# This only already deserves some benchmarks...

# Note : Adding a nodelet behavior can be done "over" existing, usual class implementation in object style... maybe via a decorator ?

# Having a bunch of nodelet means we will need to manage somehow a "virtual machine/network".
# We should define a global max CPU + RAM usage, and a per nodelet minimal frequency, maximum storage.
# The VM will tell us if we are , after combination of all of them , going overboard...

#Note : this is very erlangish... so might be worth checking pyrlang eventually...

# Note : compared to erlang, supervision tree is treated inplace, with exceptions, ie. 'python style'

