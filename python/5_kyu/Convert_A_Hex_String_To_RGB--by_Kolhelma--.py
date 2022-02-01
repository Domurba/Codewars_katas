#2021-09-22 10:16:41.950000+00:00
"""When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

+ Accepts a case-insensitive hexadecimal color string as its parameter (ex. `"#FF9933"` or `"#ff9933"`)
+ Returns a Map<String, int> with the structure `{r: 255, g: 153, b: 51}` where *r*, *g*, and *b* range from 0 through 255

**Note:** your implementation does not need to support the shorthand form of hexadecimal notation (ie `"#FFF"`)


## Example

```
"#FF9933" --> {r: 255, g: 153, b: 51}
```
"""

def hex_string_to_RGB(hex):
    hex = hex.lstrip("#")
    return {"r": int(hex[0:2], 16), "g": int(hex[2:4], 16), "b": int(hex[4:6], 16)}