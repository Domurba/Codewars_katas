#2021-07-12 18:24:11.766000+00:00
"""In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array `arr = [0, 1, 2, 5, 1, 0]` has a peak at position `3` with a value of `5` (since `arr[3]` equals `5`).

~~~if-not:php,cpp,java,csharp,fsharp
The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be `{pos: [], peaks: []}`.
~~~
~~~if:php
The output will be returned as an associative array with two key-value pairs: `'pos'` and `'peaks'`.  Both of them should be (non-associative) arrays.  If there is no peak in the given array, simply return `['pos' => [], 'peaks' => []]`.
~~~
~~~if:cpp
The output will be returned as an object of type `PeakData` which has two members: `pos` and `peaks`.  Both of these members should be `vector<int>`s.  If there is no peak in the given array then the output should be a `PeakData` with an empty vector for both the `pos` and `peaks` members.

`PeakData` is defined in Preloaded as follows:

```cpp
struct PeakData {
  vector<int> pos, peaks;
};
```
~~~
~~~if:java
The output will be returned as a ``Map<String,List<integer>>` with two key-value pairs: `"pos"` and `"peaks"`. If there is no peak in the given array, simply return `{"pos" => [], "peaks" => []}`.
~~~
~~~if:csharp
The output will be returned as a `Dictionary<string, List<int>>` with two key-value pairs: `"pos"` and `"peaks"`. 
If there is no peak in the given array, simply return `{"pos" => new List<int>(), "peaks" => new List<int>()}`.
~~~
~~~if:fsharp
The output will be returned as a record type `PeakPositionInfo` with two fields: `Pos` and `Peaks`. 
If there is no peak in the given array, simply return `{ Pos = []; Peaks = [] }`.
~~~
~~~if:cobol
For COBOL, the answer will be stored in the two tables `positions` and `peaks` provided in the linkage section. 
If there is no peak in the given array, simply set the length of both tables to 0.
Since COBOL is a 1-indexed language, the indexes stored in `peaks`  will be shifted by 1 in comparison with other languages.
~~~

Example: `pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])` should return `{pos: [3, 7], peaks: [6, 3]}` (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! `[1, 2, 2, 2, 1]` has a peak while `[1, 2, 2, 2, 3]` and `[1, 2, 2, 2, 2]` do not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: 
`pickPeaks([1, 2, 2, 2, 1])` returns `{pos: [1], peaks: [2]}` (or equivalent in other languages)

Have fun!"""

def pick_peaks(arr):
    prev, cur = 0, 0
    pos = []
    peaks = []

    for next in range(1, len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        else:
            if arr[next] < arr[cur]:
                if arr[prev] < arr[cur]:
                    pos.append(cur)
                    peaks.append(arr[cur])
                prev = cur
                cur = next

    return {"pos": pos, "peaks": peaks}