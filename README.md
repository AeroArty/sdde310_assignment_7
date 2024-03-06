In lab this week, you wrote the key components at the core of a fixed-size hash table. Unfortunately, it's not very useful without a way of handling collisions and maintaining a healthy load factor, so let's implement a couple more features.

1. Handle hash key collisions by implementing two separate hash table classes, one which utilizes chaining and another which uses linear probing such that the colliding value can be both stored and removed.
2. Secondly, write a rehashing function which will automatically rehash both classes when they reach an appropriate load factor.


Notes:

-  .75 as the threshold load factor for your probing hash table and 1.5 for your chaining hash table. Rehash only after load factor exceeds this level.
- Default both tables to a size of 10 so that I can ensure collisions are happening and that rehashing is occurring at the right time.