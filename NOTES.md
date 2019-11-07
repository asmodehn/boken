Various design notes :
  
  - most of the "data gathering" parti for boken is being done in aiokraken.

  - We need a clean interface between aiokraken and boken (see Functional Domain Modeling - Note the domain being modelled is kraken's exchange one)

  - We need a way to keep a memory of the data seen, with additional local timing information (we will want to replay and simulate local knowledge at different times). This seems more into elixir playing field: having memory of past events is mandatory as soon as you want equivalence between always running and quickly restarting process : you should minimize loss of data on process restart.  AIOKraken should provide hooks for external system wanting to "log" all meaningful/domain-relevant events.

  - We need a way to build strategy from replaying past data (ie "backtesting"), and trying to infer useful strategies from it. This seems more into julia playing field ( see GEN for differential probabilistic programming )

  - Another alternative to infer useful strategy could be to use a Echo State Network. This seems again more in python's playing field, but it should probablye be distinct from aiokraken, instead relying for "accelerated learning" into past data, or current data transparently, with an accelerated timeflow...

