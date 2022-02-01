#2021-07-13 14:32:37.240000+00:00
"""You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.  

For example in the following picture the tail's size is 3 and the loop size is 12:

<img width='320px' src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyOTcuMjUgMzE0LjQyIj48ZyBmaWxsPSIjRUMwMDhDIj48cGF0aCBkPSJNNTAuMTQgNDkuMzJsLTMuMzMtNy45My0uODIgMy4wOC0xMi42My0xMi42My0uNzEuNyAxMi42NCAxMi42NC0zLjA4Ljgxek04MC45MSA4MC4wOWwtMy4zMy03LjkyLS44MSAzLjA3LTEyLjY0LTEyLjYzLS43LjcxIDEyLjYzIDEyLjYzLTMuMDguODJ6TTExMi4xIDExMS4yOGwtMy4zMy03LjkyLS44MiAzLjA3TDk1LjMyIDkzLjhsLS43LjcxIDEyLjYzIDEyLjYzLTMuMDguODF6TTE1My43NCAxMDEuODdsLTguNTkuMDkgMi41NCAxLjkyLTIwLjQ3IDguNjEuMzkuOTIgMjAuNDYtOC42MS0uNCAzLjE2ek0yMDAuNjggMTAyLjcybC03LjUxLTQuMTkgMS4yNSAyLjkyLTIxLjQ5LTIuNjEtLjEzLjk5IDIxLjUgMi42Mi0xLjkyIDIuNTN6TTI0Mi41NSAxMjcuNjhsLTQuNDItNy4zOC0uMzcgMy4xNi0xOC42NS0xMy45OC0uNi44IDE4LjY1IDEzLjk4LTIuOTMgMS4yNHpNMjY2LjIyIDE2OS45OGwtLjE1LTguNi0xLjkgMi41Ni04LjgxLTIwLjUzLS45MS4zOSA4LjggMjAuNTMtMy4xNi0uMzh6TTI2OS42NiAxODguOTlsLS45OS0uMTQtMyAyMS4zLTIuNS0xLjk3IDIuMTEgOC4zNCA0LjMzLTcuNDMtMi45NSAxLjJ6TTI1OC41MSAyMzUuMThsLS44LS42LTE0LjU0IDE5LjI5LTEuMjQtMi45My0yLjE5IDguMzEgNy4zOS00LjQtMy4xNi0uMzh6TTIyNC4zNCAyNzEuN2wtLjM5LS45Mi0xOS45NiA4LjM1LjQxLTMuMTYtNi4wOCA2LjA4IDguNTktLjA4LTIuNTMtMS45MnpNMTc4LjE5IDI4NC4yOGwtMjEuMDYtMi42MiAxLjkzLTIuNTMtOC4zIDIuMjQgNy40OSA0LjIxLTEuMjQtMi45MyAyMS4wNiAyLjYyek0xMzIuNTEgMjczLjU0bC0xOC4xOS0xMy43NyAyLjk0LTEuMjMtOC4zMS0yLjIyIDQuMzggNy40LjM5LTMuMTYgMTguMTggMTMuNzh6TTk2LjkzIDIzOS45MWwtOC4xOS0xOS42NiAzLjE2LjQxLTYuMDYtNi4wOS4wNSA4LjU5IDEuOTMtMi41MyA4LjE5IDE5LjY3ek04OC42OSAxNzUuNTdsLTIuMjUtOC4zLTQuMjEgNy40OSAyLjkzLTEuMjRMODIuNiAxOTRsMSAuMTIgMi41NS0yMC40OHpNMTExLjM4IDEyNS4zOWwtNy40IDQuMzggMy4xNi4zOS0xMy41NSAxNy45My43OS42IDEzLjU2LTE3LjkzIDEuMjMgMi45NHoiLz48L2c+PGcgc3Ryb2tlLW1pdGVybGltaXQ9IjEwIj48Y2lyY2xlIGZpbGw9IiNBQUYiIHN0cm9rZT0iIzQxNDA0MiIgY3g9IjI2Ny42OSIgY3k9IjE3OS40NSIgcj0iOS41OSIvPjxjaXJjbGUgZmlsbD0iI0FBRiIgc3Ryb2tlPSIjNDE0MDQyIiBjeD0iMjYyIiBjeT0iMjI2LjM4IiByPSI5LjU5Ii8+PGNpcmNsZSBmaWxsPSIjQUFGIiBzdHJva2U9IiM0MTQwNDIiIGN4PSIyMzIuMzIiIGN5PSIyNjUuNjIiIHI9IjkuNTkiLz48Y2lyY2xlIGZpbGw9IiNBQUYiIHN0cm9rZT0iIzQxNDA0MiIgY3g9IjE4OC4xNiIgY3k9IjI4My45OSIgcj0iOS41OSIvPjxjaXJjbGUgZmlsbD0iI0FBRiIgc3Ryb2tlPSIjNDE0MDQyIiBjeD0iMTQxLjM5IiBjeT0iMjc4LjIxIiByPSI5LjU5Ii8+PGNpcmNsZSBmaWxsPSIjQUFGIiBzdHJva2U9IiM0MTQwNDIiIGN4PSIxMDIuMjYiIGN5PSIyNDguNTciIHI9IjkuNTkiLz48Y2lyY2xlIGZpbGw9IiNBQUYiIHN0cm9rZT0iIzQxNDA0MiIgY3g9IjgzLjkiIGN5PSIyMDQuNDIiIHI9IjkuNTkiLz48Y2lyY2xlIGZpbGw9IiNBQUYiIHN0cm9rZT0iIzQxNDA0MiIgY3g9Ijg5LjY4IiBjeT0iMTU3LjY1IiByPSI5LjU5Ii8+PGNpcmNsZSBmaWxsPSIjQUFGIiBzdHJva2U9IiM0MTQwNDIiIGN4PSIxMTkuMzEiIGN5PSIxMTguNTIiIHI9IjkuNTkiLz48Y2lyY2xlIGZpbGw9IiNBQUYiIHN0cm9rZT0iIzQxNDA0MiIgY3g9IjE2My40NyIgY3k9IjEwMC4xNSIgcj0iOS41OSIvPjxjaXJjbGUgZmlsbD0iI0FBRiIgc3Ryb2tlPSIjNDE0MDQyIiBjeD0iMjEwLjIzIiBjeT0iMTA1LjkzIiByPSI5LjU5Ii8+PGNpcmNsZSBmaWxsPSIjQUFGIiBzdHJva2U9IiM0MTQwNDIiIGN4PSIyNDkuMzMiIGN5PSIxMzUuNTMiIHI9IjkuNTkiLz48Y2lyY2xlIGZpbGw9IiNBQUYiIHN0cm9rZT0iIzQxNDA0MiIgY3g9IjI2Ny42OSIgY3k9IjE3OS40NSIgcj0iOS41OSIvPjxjaXJjbGUgZmlsbD0iI0FGQSIgc3Ryb2tlPSIjMDAwIiBjeD0iMjYuMzYiIGN5PSIyNS41NSIgcj0iOS41OSIvPjxjaXJjbGUgZmlsbD0iI0FGQSIgc3Ryb2tlPSIjMDAwIiBjeD0iNTYuOTEiIGN5PSI1Ni4xIiByPSI5LjU5Ii8+PGNpcmNsZSBmaWxsPSIjQUZBIiBzdHJva2U9IiMwMDAiIGN4PSI4OC4wNiIgY3k9Ijg3LjI1IiByPSI5LjU5Ii8+PC9nPjxwYXRoIGQ9Ik0xMjAuMyAxMjIuNTFoLTEuN3YtNS40NWgtMi4xMXYtMS4yOGMxLjE5LjAyIDIuMjgtLjM4IDIuNDYtMS42N2gxLjM2djguNHpNMTYwLjk1IDk5LjQzYy0uMDYtMS45MiAxLjAzLTMuMzkgMy4wNS0zLjM5IDEuNTQgMCAyLjg4Ljk4IDIuODggMi42MyAwIDEuMjYtLjY3IDEuOTYtMS41IDIuNTQtLjgzLjU5LTEuODEgMS4wNy0yLjQyIDEuOTNoMy45N3YxLjQ2aC02LjE2Yy4wMS0xLjk0IDEuMi0yLjc3IDIuNjUtMy43NS43NC0uNSAxLjc1LTEuMDIgMS43Ni0yLjA1IDAtLjc5LS41My0xLjMtMS4yNi0xLjMtMS4wMSAwLTEuMzMgMS4wNC0xLjMzIDEuOTNoLTEuNjR6TTIwOS42NSAxMDQuNzRjLjczLjA2IDEuNzktLjA4IDEuNzktMS4wNCAwLS43MS0uNTYtMS4xMi0xLjE5LTEuMTItLjg1IDAtMS4zMS42NC0xLjI5IDEuNWgtMS42MmMuMDYtMS43MSAxLjE3LTIuOSAyLjktMi45IDEuMzQgMCAyLjgyLjgzIDIuODIgMi4zMyAwIC43OS0uNCAxLjUtMS4xOCAxLjcxdi4wMmMuOTIuMiAxLjQ5Ljk3IDEuNDkgMS45MSAwIDEuNzYtMS40NyAyLjc2LTMuMTIgMi43Ni0xLjg4IDAtMy4xNS0xLjEzLTMuMTItMy4wNmgxLjYyYy4wNC45MS40OSAxLjY2IDEuNDggMS42Ni43NyAwIDEuMzctLjUzIDEuMzctMS4zMiAwLTEuMjctMS4xMi0xLjI1LTEuOTQtMS4yNXYtMS4yek0yNDkuNTcgMTM3LjJoLTMuNTV2LTEuNTZsMy42NS00Ljg5aDEuNTJ2NS4wNWgxLjEydjEuNGgtMS4xMnYxLjk0aC0xLjYydi0xLjk0em0wLTQuMzJoLS4wNGwtMi4xNyAyLjkyaDIuMjF2LTIuOTJ6TTI3MC40NSAxNzYuNDhoLTMuNDdsLS4zNCAxLjkxLjAyLjAyYy40Ni0uNDcuOTgtLjY1IDEuNjQtLjY1IDEuNjUgMCAyLjU5IDEuMjggMi41OSAyLjg1IDAgMS43My0xLjQzIDMuMDYtMy4xMiAzLjAyLTEuNjMgMC0zLjA5LS45LTMuMTItMi42NmgxLjdjLjA4Ljc0LjY0IDEuMjYgMS4zOCAxLjI2Ljg5IDAgMS40NS0uNzggMS40NS0xLjYyIDAtLjg4LS41NC0xLjU3LTEuNDUtMS41Ny0uNjEgMC0uOTUuMjItMS4yOC42N2gtMS41NGwuODMtNC42NGg0LjY5djEuNDF6TTI2My4xNiAyMjQuODljLS4xMS0uNTYtLjU0LTEuMDQtMS4xMy0xLjA0LTEuMjQgMC0xLjU2IDEuNjItMS42MSAyLjU1bC4wMi4wMmMuNDctLjY2IDEuMDgtLjk0IDEuODktLjk0LjcyIDAgMS40NS4zNCAxLjkzLjg2LjQ0LjUyLjY1IDEuMjEuNjUgMS44NyAwIDEuNzEtMS4xOSAzLjA3LTIuOTQgMy4wNy0yLjU0IDAtMy4yMy0yLjIyLTMuMjMtNC4zNCAwLTIuMDUuOTEtNC4zOSAzLjMtNC4zOSAxLjQ1IDAgMi41My44NSAyLjcyIDIuMzNoLTEuNnptLTIuNTggMy40NGMwIC43OC41IDEuNTYgMS4zNSAxLjU2LjgyIDAgMS4yOC0uNzggMS4yOC0xLjU0IDAtLjc5LS40MS0xLjU4LTEuMjgtMS41OC0uOTEgMC0xLjM1LjczLTEuMzUgMS41NnpNMjM1LjAzIDI2Mi44NGMtMS43NiAxLjU0LTIuNzIgNC42OS0yLjc1IDYuOTNoLTEuODJjLjE5LTIuNDggMS4yMi00Ljg5IDIuODItNi44MWgtMy45OHYtMS41OGg1LjczdjEuNDZ6TTE4OC4wMSAyODAuMjNjMi4wOSAwIDIuODEgMS40NCAyLjgxIDIuMjUgMCAuODMtLjQzIDEuNS0xLjIyIDEuNzZ2LjAyYzEgLjIzIDEuNTcgMSAxLjU3IDIuMDUgMCAxLjc2LTEuNTggMi42NC0zLjE0IDIuNjQtMS42MiAwLTMuMTktLjgyLTMuMTktMi42MyAwLTEuMDcuNi0xLjgyIDEuNTgtMi4wNnYtLjAyYy0uODItLjIzLTEuMjQtLjktMS4yNC0xLjczIDAtMS41IDEuNDctMi4yOCAyLjgzLTIuMjh6bS4wMiA3LjQ1Yy44MiAwIDEuNDQtLjU4IDEuNDQtMS40MiAwLS44LS42NS0xLjM0LTEuNDQtMS4zNC0uODMgMC0xLjQ5LjQ3LTEuNDkgMS4zMyAwIC44Ny42NyAxLjQzIDEuNDkgMS40M3ptLS4wMi0zLjljLjcgMCAxLjI2LS4zOCAxLjI2LTEuMSAwLS40My0uMi0xLjE2LTEuMjYtMS4xNi0uNjggMC0xLjI4LjQyLTEuMjggMS4xNiAwIC43My42IDEuMSAxLjI4IDEuMXpNMTQwLjk5IDI4MC4yNmMuMTEuNTYuNTQgMS4wNCAxLjEzIDEuMDQgMS4yNCAwIDEuNTYtMS42MiAxLjYxLTIuNTVsLS4wMi0uMDJjLS40Ny42Ni0xLjA4Ljk0LTEuOS45NC0uNzIgMC0xLjQ1LS4zNC0xLjkzLS44Ni0uNDQtLjUyLS42NS0xLjIxLS42NS0xLjg3IDAtMS43MSAxLjE5LTMuMDcgMi45NC0zLjA3IDIuNTQgMCAzLjIzIDIuMjIgMy4yMyA0LjM0IDAgMi4wNS0uOTEgNC4zOS0zLjMgNC4zOS0xLjQ1IDAtMi41My0uODUtMi43Mi0yLjMzaDEuNjF6bTIuNTgtMy40NGMwLS43OC0uNS0xLjU2LTEuMzYtMS41Ni0uODIgMC0xLjI4Ljc4LTEuMjggMS41NCAwIC43OS40MSAxLjU4IDEuMjggMS41OC45MSAwIDEuMzYtLjczIDEuMzYtMS41NnpNOTkuNDcgMjUyLjk0aC0xLjd2LTUuNDVoLTIuMTF2LTEuMjhjMS4xOS4wMyAyLjI4LS4zOCAyLjQ2LTEuNjdoMS4zNnY4LjR6TTEwNC43NiAyNDQuMzdjMS42OCAwIDMuMDkgMS4wNSAzLjA5IDQuMzMgMCAzLjM1LTEuNDIgNC40LTMuMDkgNC40LTEuNjYgMC0zLjA3LTEuMDUtMy4wNy00LjQgMC0zLjI3IDEuNDItNC4zMyAzLjA3LTQuMzN6bTAgNy4zM2MxLjM5IDAgMS4zOS0yLjA1IDEuMzktMyAwLS44OCAwLTIuOTMtMS4zOS0yLjkzLTEuMzcgMC0xLjM3IDIuMDUtMS4zNyAyLjkzLjAxLjk1LjAxIDMgMS4zNyAzek04MS42NSAyMDguMThoLTEuN3YtNS40NWgtMi4xMXYtMS4yOGMxLjE5LjAyIDIuMjgtLjM4IDIuNDYtMS42N2gxLjM2djguNHpNODguMzIgMjA4LjE4aC0xLjd2LTUuNDVoLTIuMTF2LTEuMjhjMS4xOS4wMiAyLjI4LS4zOCAyLjQ2LTEuNjdoMS4zNnY4LjR6TTg3LjMxIDE2MS4zOGgtMS43di01LjQ1SDgzLjV2LTEuMjhjMS4xOS4wMiAyLjI4LS4zOCAyLjQ2LTEuNjdoMS4zNnY4LjR6TTg5LjcyIDE1Ni4yMWMtLjA2LTEuOTIgMS4wMy0zLjM5IDMuMDUtMy4zOSAxLjU0IDAgMi44OC45OCAyLjg4IDIuNjMgMCAxLjI2LS42NyAxLjk2LTEuNSAyLjU0LS44My41OS0xLjgxIDEuMDctMi40MiAxLjkzaDMuOTd2MS40NmgtNi4xNmMuMDEtMS45NCAxLjItMi43NyAyLjY1LTMuNzUuNzQtLjUgMS43NS0xLjAyIDEuNzYtMi4wNSAwLS43OS0uNTMtMS4zLTEuMjYtMS4zLTEuMDEgMC0xLjMzIDEuMDQtMS4zMyAxLjkzaC0xLjY0ek0yNS41NSAyMC44N2gxLjkzbDMuMiA4LjU2aC0xLjk2bC0uNjUtMS45MWgtMy4ybC0uNjcgMS45MWgtMS45bDMuMjUtOC41NnptLS4xOCA1LjI1aDIuMjJsLTEuMDgtMy4xNGgtLjAybC0xLjEyIDMuMTR6TTUzLjc2IDUxLjk5aDQuMDNjMS42MyAwIDIuNzMuNTMgMi43MyAyLjEyIDAgLjg0LS40MiAxLjQzLTEuMTYgMS43OSAxLjA0LjMgMS41NyAxLjEgMS41NyAyLjE3IDAgMS43NC0xLjQ4IDIuNDgtMy4wMiAyLjQ4aC00LjE1di04LjU2em0xLjg4IDMuNDZoMS45MWMuNjYgMCAxLjE1LS4zIDEuMTUtMS4wMiAwLS44Mi0uNjItLjk4LTEuMjktLjk4aC0xLjc2djJ6bTAgMy42NGgyLjAxYy43NCAwIDEuMzktLjI0IDEuMzktMS4xMyAwLS44OC0uNTUtMS4yMi0xLjM1LTEuMjJoLTIuMDV2Mi4zNXpNOTAuNDMgODUuODhjLS4xMi0uODUtLjk0LTEuNS0xLjg3LTEuNS0xLjY5IDAtMi4zMyAxLjQ0LTIuMzMgMi45NCAwIDEuNDMuNjQgMi44NyAyLjMzIDIuODcgMS4xNSAwIDEuOC0uNzkgMS45NC0xLjkyaDEuODJjLS4xOSAyLjEzLTEuNjcgMy41LTMuNzcgMy41LTIuNjUgMC00LjIxLTEuOTgtNC4yMS00LjQ1IDAtMi41NCAxLjU2LTQuNTIgNC4yMS00LjUyIDEuODggMCAzLjQ3IDEuMSAzLjY5IDMuMDhoLTEuODF6Ii8+PC9zdmc+' />


```ruby
# Use the `next' method to get the following node.
node.next
```
```javascript
// Use the `getNext' method or 'next' property to get the following node.
node.getNext()
node.next
```
```python
# Use the `next' attribute to get the following node
node.next
```
```java
// Use the `getNext()` method to get the following node.
node.getNext()
```
```haskell
-- use the `next :: Node a -> Node a` function to get the following node
```
```cs
# Use the `next' method to get the following node.
node.next
```
```c
// Use the `next` field to get the following node.
Node* nextNode = nodePtr->next;
```
```cpp
// Use the `getNext()` method to get the following node.
nodePtr->getNext()
```
~~~if:php
Use the `Node::getNext()` instance method to get the following node.

```php
$node->getNext();
```
~~~
~~~if:kotlin
Use the `Node.next` to get the next following node.

```kotlin
node.next
```
~~~


Note: do NOT mutate the nodes!

> Thanks to shadchnev, I broke all of the methods from the Hash class.

> Don't miss dmitry's article in the discussion after you pass the Kata !! """

def loop_size(node):
    temp = True
    new_node = node
    result = []
    while temp:
        result.append(new_node)
        new_node = new_node.next
        if new_node in result:
            temp = False
            loop_size = len(result) - result.index(new_node.next) + 1
    if loop_size == 2:
        return loop_size -1
    else:
        return loop_size