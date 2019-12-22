Design decisions
================

- This models a generic barter system. As a special case, a currency can be traded. 
- Units are enforced (types + contracts). TODO : follow similar design with pint to allow cooperation...
- We expect users to extend Asset with other models (like we do here for currency)
- Asset/Currency are classes and domain models must be instances (since types are not powerful enough we wwill use contracts on instances instead)
- Since Domain models for Assets are instances, they cannot instantiate "entities" on their own, so we add a float (categorical product style) and provide a class that can be used as type by a domain model, adding consistency check on the Asset...
- numbers are ingested and spitted as string, to avoid problems with precision in the various formats.
